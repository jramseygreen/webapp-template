import RolesIndexView from '@/views/dashboard/role/RolesIndexView.vue'
import RoleIndexView from '@/views/dashboard/role/partials/RoleIndexView.vue'
import AllRolesView from '@/views/dashboard/role/partials/AllRolesView.vue'
import CreateRoleView from '@/views/dashboard/role/partials/CreateRoleView.vue'
import ReadRoleView from '@/views/dashboard/role/partials/partials/ReadRoleView.vue'
import UpdateRoleView from '@/views/dashboard/role/partials/partials/UpdateRoleView.vue'
import DeleteRoleView from '@/views/dashboard/role/partials/partials/DeleteRoleView.vue'

export default {
  path: 'roles',
  name: 'RolesIndexView',
  component: RolesIndexView,
  meta: {
    allows: ['admin']
  },
  redirect: { name: 'AllRolesView' },
  children: [
    {
      path: '',
      name: 'AllRolesView',
      component: AllRolesView,
    },
    {
      path: 'create',
      name: 'CreateRoleView',
      component: CreateRoleView
    },
    {
      path: ':id',
      name: 'RoleIndexView',
      component: RoleIndexView,
      props: true,
      redirect: {name: 'ReadRoleView'},
      children: [
        {
          path: '',
          name: 'ReadRoleView',
          component: ReadRoleView,
          props: true
        },
        {
          path: 'update',
          name: 'UpdateRoleView',
          component: UpdateRoleView,
          props: true
        },
        {
          path: 'delete',
          name: 'DeleteRoleView',
          component: DeleteRoleView,
          props: true
        },
      ]
    },

  ]
}
