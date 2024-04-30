import axios from 'axios'
import type { Response } from '@/types/response'
import type { TokenData, RefreshTokenData } from '@/types/resources/auth'
import type { LoginPayload } from '@/types/payloads/auth'

export const login = (payload: LoginPayload): Promise<Response<TokenData>> => axios.post('/auth/login', payload)
export const refreshAuthToken = (refreshToken: string | null): Promise<Response<RefreshTokenData>> => axios.post('/auth/refresh', {}, { headers: { Authorization: `Bearer ${refreshToken}` }})
export const blacklistToken = (): Promise<Response> => axios.delete('/auth/blacklist-token')
export const blacklistRefreshToken = (refreshToken: string | null): Promise<Response> => axios.delete('/auth/blacklist-refresh-token', { headers: { Authorization: `Bearer ${refreshToken}` }})
