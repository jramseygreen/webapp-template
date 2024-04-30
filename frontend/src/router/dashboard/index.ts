import DashboardView from '@/views/dashboard/DashboardView.vue'
import profile from './profile'
import user from './user'
import role from './role'
import setting from './setting'

export default {
  path: '/dashboard',
  name: 'DashboardView',
  component: DashboardView,
  redirect: {name: 'ProfileIndexView'},
  meta: {
    requiresAuth: true
  },
  children: [
    profile,
    user,
    role,
    setting
  ]
}
