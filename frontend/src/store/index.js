import Vue from 'vue'
import Vuex from 'vuex'
import data from './modules/data'
import searchData from './modules/searchData'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    data,
    searchData,
  },
})
