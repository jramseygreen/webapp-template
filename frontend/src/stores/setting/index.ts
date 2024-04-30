import { defineStore } from 'pinia'
import type { UpdateSettingPayload, UpdateAllSettingsPayload } from '@/types/payloads/setting'
import type { Setting } from '@/types/resources/setting'
import type { Response } from '@/types/response'
import { allSettings, readSetting, updateSetting, updateAllSettings } from '@/services/setting'

interface SettingState {
  setting: null | Setting,
  settings: Setting[]
}

export const useSettingStore  = defineStore('SettingStore', {
  state: (): SettingState => {
    return {
      setting: null,
      settings: []
    }
  },
  actions: {
    allSettings(): Promise<Response<Setting[]>> {
      return allSettings().then((response: Response<Setting[]>) => {
        this.settings = response.data
        return response
      })
    },
    readSetting(name: string): Promise<Response<Setting>> {
      return readSetting(name).then((response: Response<Setting>) => {
        this.setting = response.data
        return response
      })
    },
    updateAllSettings(payload: UpdateAllSettingsPayload): Promise<Response<Setting[]>> {
      return updateAllSettings(payload).then((response: Response<Setting[]>) => {
        this.settings = response.data
        return response
      })
    },
    updateSetting(payload: UpdateSettingPayload): Promise<Response<Setting>> {
      return updateSetting(payload).then((response: Response<Setting>) => {
        this.setting = response.data
        let index = this.settings.indexOf(this.setting)
        if (index) {
          this.settings[index] = this.setting
        }
        return response
      })
    }
  },
  getters: {
    isRegistrationEnabled: (state) => !!state.settings.find(setting => setting.name === 'REGISTRATION_ENABLED')?.value,
    isLoginForced: (state) => !!state.settings.find(setting => setting.name === 'FORCE_LOGIN')?.value
  }
})
