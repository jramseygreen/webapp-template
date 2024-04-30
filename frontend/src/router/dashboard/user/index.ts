import UsersIndexView from '@/views/dashboard/user/UsersIndexView.vue'
import UserIndexView from '@/views/dashboard/user/partials/UserIndexView.vue'
import AllUsersView from '@/views/dashboard/user/partials/AllUsersView.vue'
import CreateUserView from '@/views/dashboard/user/partials/CreateUserView.vue'
import ReadUserView from '@/views/dashboard/user/partials/partials/ReadUserView.vue'
import UpdateUserView from '@/views/dashboard/user/partials/partials/UpdateUserView.vue'
import DeleteUserView from '@/views/dashboard/user/partials/partials/DeleteUserView.vue'

export default {
  path: 'users',
  name: 'UsersIndexView',
  component: UsersIndexView,
  meta: {
    allows: ['admin']
  },
  redirect: {name: 'AllUsersView'},
  children: [
    {
      path: '',
      name: 'AllUsersView',
      component: AllUsersView,
    },
    {
      path: 'create',
      name: 'CreateUserView',
      component: CreateUserView
    },
    {
      path: ':id',
      name: 'UserIndexView',
      component: UserIndexView,
      props: true,
      redirect: {name: 'ReadUserView'},
      children: [
        {
          path: '',
          name: 'ReadUserView',
          component: ReadUserView,
          props: true
        },
        {
          path: 'update',
          name: 'UpdateUserView',
          component: UpdateUserView,
          props: true
        },
        {
          path: 'delete',
          name: 'DeleteUserView',
          component: DeleteUserView,
          props: true
        },
      ]
    },

  ]
}
