import SettingsIndexView from '@/views/dashboard/setting/SettingsIndexView.vue'
import ManageSettingsView from '@/views/dashboard/setting/partials/ManageSettingsView.vue'

export default {
  path: 'settings',
  name: 'SettingsIndexView',
  component: SettingsIndexView,
  redirect: {name: 'ManageSettingsView'},
  meta: {
    allows: ['admin']
  },
  children: [
    {
      path: '',
      name: 'ManageSettingsView',
      component: ManageSettingsView
    }
  ]
}
