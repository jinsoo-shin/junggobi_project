import api from '../../api'

const state = {
  items : [],
  favoriteItems : [],
}
const getters = {
  getFavoriteItems(state) {
    return state.favoriteItems;
  },
  getItems(state) {
    console.log(state.items)
    return state.items;
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
  async test1() {
    const resp = await api.test()
    state.items = resp.data
  }
}
export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
}
