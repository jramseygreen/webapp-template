import axios from 'axios'
import type { Response } from '@/types/response'
import type { Setting } from '@/types/resources/setting'
import type { UpdateSettingPayload, UpdateAllSettingsPayload } from '@/types/payloads/setting'

export const allSettings = (): Promise<Response<Setting[]>> => axios.get('/settings')
export const updateAllSettings = (payload: UpdateAllSettingsPayload): Promise<Response<Setting[]>> => axios.patch('/settings', payload)
export const readSetting = (name: string): Promise<Response<Setting>> => axios.get(`/settings/${name}`)
export const updateSetting = (payload: UpdateSettingPayload): Promise<Response<Setting>> => axios.patch(`/settings/${payload.name}`, payload)
