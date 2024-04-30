import { createRouter, createWebHistory } from 'vue-router'
import type { RouteRecordRaw, Router, RouteLocationNormalized } from 'vue-router';
import { useAuthStore } from '@/stores/auth'
import { useIdentityStore } from '@/stores/auth/identity'
import { useSettingStore } from '@/stores/setting'
import { useToast } from 'vue-toastification'
import dashboard from './dashboard'
import errors from './errors'
import HomeView from '@/views/HomeView.vue'
import LoginView from '@/views/auth/LoginView.vue'
import RegisterView from '@/views/auth/RegisterView.vue'
import PageOneView from '@/views/pages/PageOneView.vue'
import PageTwoView from '@/views/pages/PageTwoView.vue'



export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView,
      props: (route: RouteLocationNormalized) => {
        return {
          redirect: route.query.redirect
        }
      }
    },
    {
      path: '/register',
      name: 'RegisterView',
      component: RegisterView
    },
    {
      path: '/page-1',
      name: 'PageOneView',
      component: PageOneView
    },
    {
      path: '/page-2',
      name: 'PageTwoView',
      component: PageTwoView
    },
    dashboard,
    errors
  ]
})


const toast = useToast()

router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  const identityStore = useIdentityStore()
  const settingStore = useSettingStore()

  if (!settingStore.settings.length) {
    await settingStore.allSettings()
  }

  // Check if the current route is already the unauthorized or forbidden view
  if (to.name === 'LoginView' || to.name === 'RegisterView' || to.name === 'UnauthorizedView' || to.name === 'ForbiddenView') {
    // Skip redirection logic
    next();
    return;
  }

  // if login is forced and browse to the home page, push straight to login
  if (settingStore.isLoginForced && !authStore.isAuthed && to.name === 'HomeView') {
    next({name: 'LoginView'})
    return
  }

  // Check permissions for each matched route
  // Flag to track if redirection occurred
  let redirectionOccurred = false;

  to.matched.every(route => {
    // Check if the route requires authentication
    if ((settingStore.isLoginForced || route.meta.requiresAuth) && !authStore.isAuthed) {
      // User is not authenticated, redirect to unauthorized view
      toast.error('Please login to view this resource')
      next({ name: 'UnauthorizedView', query: {redirect: to.name as string}});
      redirectionOccurred = true;
      return false; // Break out of the loop
    }

    const allows = route.meta.allows as string[] | undefined;
    const blocks = route.meta.blocks as string[] | undefined;

    // Check if the route has allows meta and user has the required role
    if (allows) {
      for (const role of allows) {
        if (!identityStore.hasRole(role)) {
          // User doesn't have the required role, redirect to forbidden view
          toast.error('Additional permissions required')
          next({ name: 'ForbiddenView' });
          redirectionOccurred = true;
          return false; // Break out of the loop
        }
      }
    }

    // Check if the route has blocks meta and user has the blocked role
    if (blocks) {
      for (const role of blocks) {
        if (identityStore.hasRole(role)) {
          // User has a blocked role, redirect to forbidden view
          toast.error('Additional permissions required')
          next({ name: 'ForbiddenView' });
          redirectionOccurred = true;
          return false; // Break out of the loop
        }
      }
    }

    return true; // Continue to the next iteration of the loop
  });

  // If no redirection occurred, continue navigation
  if (!redirectionOccurred) {
    next();
  }
});

export default router;
