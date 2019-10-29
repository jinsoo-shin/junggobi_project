import Vue from 'vue'
import Router from 'vue-router'
import ItemDetailPage from './pages/ItemDetailPage.vue'
import Main from './pages/Main.vue'
import RedirectPage from './pages/RedirectPage.vue'
import Home from './pages/Home.vue'

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
    },
    {
      path: '/redirectPage',
      name: 'redirectPage',
      component: RedirectPage,
      props: true
    },
    {
      path: '/home',
      name: 'home',
      component: Home
    }
  ]
})
