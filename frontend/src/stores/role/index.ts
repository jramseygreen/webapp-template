import { defineStore } from 'pinia'
import type { CreateRolePayload, UpdateRolePayload } from '@/types/payloads/role'
import type { Role } from '@/types/resources/role'
import type { Response } from '@/types/response'
import { allRoles, createRole, readRole, updateRole, deleteRole } from '@/services/role'

interface RoleState {
  role: null | Role,
  roles: Role[]
}

export const useRoleStore  = defineStore('RoleStore', {
  state: (): RoleState => {
    return {
      role: null,
      roles: []
    }
  },
  actions: {
    allRoles(): Promise<Response<Role[]>> {
      return allRoles().then((response: Response<Role[]>) => {
        this.roles = response.data
        return response
      })
    },
    createRole(payload: CreateRolePayload): Promise<Response<Role>> {
      return createRole(payload).then((response: Response<Role>) => {
        if (this.roles.length) {
          this.roles.push(response.data)
        }
        return response
      })
    },
    readRole(id: number): Promise<Response<Role>> {
      return readRole(id).then((response: Response<Role>) => {
        this.role = response.data
        return response
      })
    },
    updateRole(payload: UpdateRolePayload): Promise<Response<Role>> {
      return updateRole(payload).then((response: Response<Role>) => {
        this.role = response.data
        let index = this.roles.indexOf(this.role)
        if (index) {
          this.roles[index] = this.role
        }
        return response
      })
    },
    deleteRole(id: number): Promise<Response> {
      return deleteRole(id).then((response: Response) => {
        this.roles = this.roles.filter((role: Role) => role.id !== id)
        this.role = null
        return response
      })
    }
  },
  getters: {

  }
})
