import { defineStore } from 'pinia'
import type { CreateIdentityPayload, UpdateIdentityPayload, DeleteIdentityPayload } from '@/types/payloads/auth/identity'
import type { User } from '@/types/resources/user'
import type { Role } from '@/types/resources/role'
import type { Response } from '@/types/response'
import { createIdentity, readIdentity, updateIdentity, deleteIdentity } from '@/services/auth/identity'

interface IdentityState {
  identity: null | User
}

export const useIdentityStore  = defineStore('IdentityStore', {
  state: (): IdentityState => {
    return {
      identity: null,
    }
  },
  actions: {
    createIdentity(payload: CreateIdentityPayload): Promise<Response<User>> {
      return createIdentity(payload)
    },
    readIdentity(): Promise<Response<User>> {
      return readIdentity().then((response: Response<User>) => {
        this.identity = response.data
        return response
      })
    },
    updateIdentity(payload: UpdateIdentityPayload): Promise<Response<User>> {
      return updateIdentity(payload).then((response: Response<User>) => {
        this.identity = response.data
        return response
      })
    },
    deleteIdentity(payload: DeleteIdentityPayload): Promise<Response> {
      return deleteIdentity(payload).then((response: Response) => {
        this.identity = null
        return response
      })
    },
    hasRole(name: string) {
      return !!this.identity?.roles?.map((role: Role) => role.name)?.includes(name)
    }
  },
  getters: {

  }
})
