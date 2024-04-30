import axios from 'axios'
import type { Response } from '@/types/response'
import type { User } from '@/types/resources/user'
import type { CreateUserPayload, UpdateUserPayload } from '@/types/payloads/user'

export const allUsers = (): Promise<Response<User[]>> => axios.get('/users')
export const createUser = (payload: CreateUserPayload): Promise<Response<User>> => axios.post(`/users`, payload)
export const readUser = (id: number): Promise<Response<User>> => axios.get(`/users/${id}`)
export const updateUser = (payload: UpdateUserPayload): Promise<Response<User>> => axios.patch(`/users/${payload.id}`, payload)
export const deleteUser = (id: number): Promise<Response> => axios.delete(`/users/${id}`)
