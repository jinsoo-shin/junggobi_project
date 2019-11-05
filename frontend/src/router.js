import Vue from 'vue'
import Router from 'vue-router'
import SearchPage from './pages/searchPage.vue'
import Main from './pages/Main.vue'
import RedirectPage from './pages/RedirectPage.vue'
import BlogPage from './pages/BlogPage.vue'
import ItemPage from './pages/ItemPage.vue'

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
            path: '/search',
            name: 'searchPage',
            component: SearchPage,
            props: true
        },
        {
            path: '/redirect',
            name: 'redirectPage',
            component: RedirectPage,
            props: true
        },
        {
            path: '/blog',
            name: 'BlogPage',
            component: BlogPage,
            props: true
        },
        {
            path: '/item',
            name: 'itemPage',
            component: ItemPage,
            props: true
        }
    ]
})