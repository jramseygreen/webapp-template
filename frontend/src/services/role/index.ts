import axios from 'axios'
import type { Response } from '@/types/response'
import type { Role } from '@/types/resources/role'
import type { CreateRolePayload, UpdateRolePayload } from '@/types/payloads/role'

export const allRoles = (): Promise<Response<Role[]>> => axios.get('/roles')
export const createRole = (payload: CreateRolePayload): Promise<Response<Role>> => axios.post(`/roles`, payload)
export const readRole = (id: number): Promise<Response<Role>> => axios.get(`/roles/${id}`)
export const updateRole = (payload: UpdateRolePayload): Promise<Response<Role>> => axios.patch(`/roles/${payload.id}`, payload)
export const deleteRole = (id: number): Promise<Response> => axios.delete(`/roles/${id}`)
