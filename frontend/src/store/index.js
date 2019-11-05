import Vue from 'vue'
import Vuex from 'vuex'
import data from './modules/data'
// chatkit
import VuexPersistence from 'vuex-persist'
import chat from './modules/chat'

Vue.use(Vuex)
// chatkit
const debug = process.env.NODE_ENV !== 'production'

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

export default new Vuex.Store({
  modules: {
    data,
    // chatkit
    chat,
    plugins: [vuexLocal.plugin],
    strict: debug
  },
})
