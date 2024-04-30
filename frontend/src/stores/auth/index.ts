import {defineStore} from 'pinia'
import axios from 'axios';
import type { LoginPayload } from '@/types/payloads/auth'
import { login, refreshAuthToken, blacklistToken, blacklistRefreshToken } from '@/services/auth'
import type { Response } from '@/types/response'
import type { TokenData, RefreshTokenData } from '@/types/resources/auth'
import { useIdentityStore } from './identity'

interface AuthState {
  token: null | string
  refreshToken: null | string
}

export const useAuthStore  = defineStore('AuthStore', {
  state: (): AuthState => {
    return {
      token: localStorage.getItem('token'),
      refreshToken: localStorage.getItem('refresh_token'),
    }
  },
  actions: {
    login(payload: LoginPayload): Promise<Response<TokenData>> {
        return login(payload)
          .then(async (response: Response<TokenData>) => {
            this.token = response.data.token
            this.refreshToken = response.data.refresh_token
            axios.defaults.headers.Authorization = `Bearer ${this.token}`
            await useIdentityStore().readIdentity()
            if (this.refreshToken) {
              localStorage.setItem('token', this.token)
              localStorage.setItem('refresh_token', this.refreshToken)
            }
            return response
          })
    },
    renewToken(): Promise<Response<RefreshTokenData>> {
        return refreshAuthToken(this.refreshToken)
          .then((response: Response<RefreshTokenData>) => {
            this.token = response.data.token
            axios.defaults.headers.Authorization = `Bearer ${this.token}`
            localStorage.setItem('token', this.token)
            return response
          })
    },
    logout() {
        blacklistToken().then(() => {
          this.token = null
          localStorage.removeItem('token')
        })
        if (this.refreshToken) {
          blacklistRefreshToken(this.refreshToken).then(() => {
            this.refreshToken = null
            localStorage.removeItem('refresh_token')
          })
        }
        axios.defaults.headers.Authorization = null
        useIdentityStore().identity = null
      }
  },
  getters: {
    isAuthed: (state) => !!state.token
  }
})
