import { defineStore } from 'pinia'
import type { CreateUserPayload, UpdateUserPayload } from '@/types/payloads/user'
import type { User } from '@/types/resources/user'
import type { Response } from '@/types/response'
import { allUsers, createUser, readUser, updateUser, deleteUser } from '@/services/user'

interface UserState {
  user: null | User,
  users: User[]
}

export const useUserStore  = defineStore('UserStore', {
  state: (): UserState => {
    return {
      user: null,
      users: []
    }
  },
  actions: {
    allUsers(): Promise<Response<User[]>> {
      return allUsers().then((response: Response<User[]>) => {
        this.users = response.data
        return response
      })
    },
    createUser(payload: CreateUserPayload): Promise<Response<User>> {
      return createUser(payload).then((response: Response<User>) => {
        return response
      })
    },
    readUser(id: number): Promise<Response<User>> {
      return readUser(id).then((response: Response<User>) => {
        this.user = response.data
        return response
      })
    },
    updateUser(payload: UpdateUserPayload): Promise<Response<User>> {
      return updateUser(payload).then((response: Response<User>) => {
        this.user = response.data
        return response
      })
    },
    deleteUser(id: number): Promise<Response> {
      return deleteUser(id).then((response: Response) => {
        this.user = null
        return response
      })
    }
  },
  getters: {

  }
})
