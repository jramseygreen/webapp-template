import axios from 'axios'
import type { Response } from '@/types/response'
import type { CreateIdentityPayload, UpdateIdentityPayload,DeleteIdentityPayload } from '@/types/payloads/auth/identity'
import type { User } from '@/types/resources/user'

export const createIdentity = (payload: CreateIdentityPayload): Promise<Response> => axios.post('/auth/identity', payload)
export const readIdentity = (): Promise<Response<User>> => axios.get('/auth/identity')
export const updateIdentity = (payload: UpdateIdentityPayload): Promise<Response> => axios.patch('/auth/identity', payload)
export const deleteIdentity = (payload: DeleteIdentityPayload): Promise<Response> => axios.delete('/auth/identity', { data: payload })
