export interface UpdateSettingPayload {
  name: string
  value: string | number | boolean
  description: string
}

export interface UpdateAllSettingsPayload {
  settings: UpdateSettingPayload[];
}
