import api from '../../api'

const state = {
  favoriteItems : [],
  abc : "Dfsfsfsf"
}
const getters = {
  getFavoriteItems(state) {
    return state.favoriteItems;
  }
}
const mutations = {
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
}
const actions = {

}
export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
