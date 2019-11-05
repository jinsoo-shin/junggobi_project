import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store'
import { setupComponents } from './config/setup-components';
import swalPlugin from './plugins/VueSweetalert2';
// import './plugins/base';
import HistogramSlider from "vue-histogram-slider";
import "vue-histogram-slider/dist/histogram-slider.css";
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

// chatkit

// import VueChatScroll from "vue-chat-scroll";
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap-vue/dist/bootstrap-vue.css'
// import './assets/css/loading.css'
// import './assets/css/loading-btn.css'

Vue.use(BootstrapVue)
Vue.component(HistogramSlider.name, HistogramSlider);
Vue.use(swalPlugin);
Vue.config.productionTip = false
Vue.prototype.EventBus = new Vue();
setupComponents(Vue);

// chatkit
// Vue.use(VueChatScroll)

new Vue({
    router,
    vuetify,
    store,
    render: h => h(App)
}).$mount('#app')
