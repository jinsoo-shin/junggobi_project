import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    favoriteItems : [],
  },
  getters: {
    getFavoriteItems(state) {
      console.log(state.favoriteItems)
      return state.favoriteItems;
    }
  },
  mutations: {
    setAddFavoriteItems(state, payload){
      state.favoriteItems[state.favoriteItems.length] = payload;
    },
  },
  actions: {

  }
})
