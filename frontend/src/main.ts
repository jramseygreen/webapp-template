import '@/assets/index.css'

import { createApp } from 'vue'
import App from './App.vue'
import { router } from './router'

import Toast from 'vue-toastification'
import type { PluginOptions } from 'vue-toastification'
import 'vue-toastification/dist/index.css'

import { createPinia } from 'pinia'

import { library, dom } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'

import setupAxios from '@/composables/setupAxios'
import { useAuthStore } from '@/stores/auth'
import { useIdentityStore } from '@/stores/auth/identity'

const app = createApp(App)

const setupApp = async () => {
  const baseUrl = '/api'
  const tokenRefreshUrl = '/auth/refresh'
  const toastOptions: PluginOptions = {
    timeout: 4000
  };
  library.add(fas, far, fab)
  dom.watch()

  app.use(createPinia())

  setupAxios(baseUrl, tokenRefreshUrl)
  if (useAuthStore().isAuthed) {
    await useIdentityStore().readIdentity()
  }

  app.use(Toast, toastOptions);
  app.use(router)

}

setupApp().finally(() => app.mount('#app'))
