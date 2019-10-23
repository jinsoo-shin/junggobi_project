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
    setAddFavoriteItems(state, payload) {
      state.favoriteItems[state.favoriteItems.length] = payload;
    },
    setDeleteFavoriteItems(state,payload) {
      for(var i=0; i<state.favoriteItems.length; i++){
        if(state.favoriteItems[i].idx === payload){
          state.favoriteItems.splice(i, 1);
          break;
        }
      }
    }
  },
  actions: {

  }
})
