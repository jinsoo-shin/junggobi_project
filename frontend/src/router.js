import Vue from 'vue'
import Router from 'vue-router'
import SearchPage from './pages/searchPage.vue'
import Main from './pages/Main.vue'
import RedirectPage from './pages/RedirectPage.vue'
import BlogPage from './pages/BlogPage.vue'
import ItemPage from './pages/ItemPage.vue'
// chatkit
import Login from './views/Login.vue'
import ChatDashboard from './views/ChatDashboard.vue'

Vue.use(Router)

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [{
            path: '/',
            name: 'main',
            component: Main
        },
        {
            path: '/searchPage',
            name: 'searchPage',
            component: SearchPage,
            props: true
        },
        {
            path: '/redirectPage',
            name: 'redirectPage',
            component: RedirectPage,
            props: true
        },
        {
            path: '/BlogPage',
            name: 'BlogPage',
            component: BlogPage,
            props: true
        },
        {
            path: '/ItemPage',
            name: 'itemPage',
            component: ItemPage,
            props: true
        },
        // chatkit
        {
            path: '/',
            name: 'login',
            component: Login
        },
        {
            path: '/chat',
            name: 'chat',
            component: ChatDashboard,
        }
    ]
})