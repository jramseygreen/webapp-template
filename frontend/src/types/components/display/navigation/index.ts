import type { RouteLocationRaw } from 'vue-router';

export interface MenuItem {
  name: string
  icon?: string
  url?: RouteLocationRaw
  method?: Function
  showWithAuthentication?: boolean
  allows?: string[]
  blocks?: string[]
  isDisabled?: boolean
}
