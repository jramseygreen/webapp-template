import ProfileIndexView from '@/views/dashboard/profile/ProfileIndexView.vue'
import ReadProfileView from '@/views/dashboard/profile/partials/ReadProfileView.vue'
import UpdateProfileView from '@/views/dashboard/profile/partials/UpdateProfileView.vue'
import DeleteProfileView from '@/views/dashboard/profile/partials/DeleteProfileView.vue'

export default {
  path: 'profile',
  name: 'ProfileIndexView',
  component: ProfileIndexView,
  redirect: {name: 'ReadProfileView'},
  children: [
    {
      path: '',
      name: 'ReadProfileView',
      component: ReadProfileView
    },
    {
      path: 'update',
      name: 'UpdateProfileView',
      component: UpdateProfileView
    },
    {
      path: 'delete',
      name: 'DeleteProfileView',
      component: DeleteProfileView
    },
  ]
}
