import Vue from 'vue'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify';
import store from './store'
import { setupComponents } from './config/setup-components';
import swalPlugin from './plugins/VueSweetalert2';

Vue.use(swalPlugin);
Vue.config.productionTip = false
Vue.prototype.EventBus = new Vue();
setupComponents(Vue);

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount('#app')
