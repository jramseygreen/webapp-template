import type { RouteLocationNormalized } from 'vue-router'

import ErrorIndexView from '@/views/errors/ErrorIndexView.vue'
import UnauthorizedView from '@/views/errors/partials/UnauthorizedView.vue'
import DefaultErrorView from '@/views/errors/partials/DefaultErrorView.vue'

export default {
  path: '/error',
  name: 'ErrorIndexView',
  component: ErrorIndexView,
  redirect: {name: 'DefaultErrorView'},
  children: [
    {
      path: '',
      name: 'DefaultErrorView',
      component: DefaultErrorView
    },
    {
      path: 'unauthorized',
      name: 'UnauthorizedView',
      component: UnauthorizedView,
      props: (route: RouteLocationNormalized) => {
        return {
          title: '401 Unauthorized',
          description: "Sorry but you cannot access this resource!",
          redirect: route.query.redirect
        }
      }
    },
    {
      path: 'forbidden',
      name: 'ForbiddenView',
      component: DefaultErrorView,
      props: {
        title: '403 Forbidden',
        description: "Sorry but you do not have permission to do that"
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFoundView',
      component: DefaultErrorView,
      props: {
        title: '404 Page Not Found',
        description: "Oops! The page you are looking for doesn't exist."
      }
    }
  ]
}
