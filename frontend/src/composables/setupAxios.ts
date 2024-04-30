import axios from 'axios';
import { router } from '@/router';
import { useToast } from 'vue-toastification'
import { useAuthStore } from '@/stores/auth'

export default (baseUrl: string, tokenRefreshUrl: string) => {
  axios.defaults.baseURL = baseUrl;
  const authStore = useAuthStore()
  if (authStore.isAuthed) {
    axios.defaults.headers.Authorization = `Bearer ${authStore.token}`
  }

  // deal with JWT token refresh
  // returns only the json response data
  axios.interceptors.response.use(
  (response) => {
    // Return a successful response back to the calling service
    return response.data;
  },
  (error) => {
    // Handle errors
    if (error.response?.data) {
      const errorType = error.response.data.error_type || '';

      // if error is jwt error
      if (errorType.startsWith('jwt')) {
        // send to unauthorized page if not authenticated, token has been revoked, or refresh failed
        if (!authStore.isAuthed || errorType === 'jwt_revoked' || error.config.url === tokenRefreshUrl || (errorType === 'jwt_expired' && !authStore.refreshToken)) {
          authStore.token = null
          localStorage.removeItem('token')
          // if refresh token has expired send straight to login
          if (errorType === 'jwt_expired') {
            authStore.refreshToken = null
            localStorage.removeItem('refresh_token')
            router.push({ name: 'LoginView', query: {redirect: router.currentRoute.value.name as string} });
          } else {
            router.push({ name: 'UnauthorizedView', query: {redirect: router.currentRoute.value.name as string} });
          }
          return Promise.reject(error.response);
        }

        // jwt fresh is only used for temporary tokens
        // we must have a refresh token to attempt to refresh
        if (errorType !== 'jwt_fresh' && authStore.refreshToken) {
          // Try to refresh the token and resend the request
          return authStore.renewToken()
            .then(() => {
              const config = error.config;
              config.headers['Authorization'] = `Bearer ${authStore.token}`;
              return axios.request(config);
            })
            .catch((refreshError) => {
              return Promise.reject(refreshError);
            });
          }
      }
    }

    // Return any error that is not related to authorization
    return Promise.reject(error.response);
  }
);

  // show a toast notification if it's an error
  const toast = useToast()

  axios.interceptors.response.use(
    (response) => {
      return response;
    },
    (error) => {
      // if there is no data it means it was from a token refresh attempt and will therefore double up the error message
      if (error.data?.message) {
        console.log(error)
        toast.error(error.data.message);
        return Promise.reject(error.data);
      }
      return Promise.reject(error);
    }
  );
}
