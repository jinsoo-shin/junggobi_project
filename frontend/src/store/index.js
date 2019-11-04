import Vue from 'vue'
import Vuex from 'vuex'
import data from './modules/data'
// chat
import VuexPersistence from 'vuex-persist'
import chat from './modules/chat'

Vue.use(Vuex)

// chat
// vuex-persist패키지는 우리의 Vuex 상태 페이지를 다시로드 또는 새로 고침 사이에 저장되도록합니다
const debug = process.env.NODE_ENV !== 'production'

const vuexLocal = new VuexPersistence({
  storage: window.localStorage
})

export default new Vuex.Store({
  modules: {
    data,
    // chat
    chat,
    plugins: [vuexLocal.plugin],
    strict: debug,
  },
})
