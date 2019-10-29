import Vue from 'vue'
import Router from 'vue-router'
import ItemDetailPage from './pages/ItemDetailPage.vue'
import Main from './pages/Main.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'main',
      component: Main
    },
    {
      path: '/itemDetailPage',
      name: 'itemDetailPage',
      component: ItemDetailPage
    }
  ]
})
