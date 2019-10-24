

const state = {
    selected : [],
  }
  const getters = {
    getSelected(state) {
      return state.selected;
    }
  }
  const mutations = {
    setAddSelected(state, payload) {
      state.favoriteItems[state.favoriteItems.length] = payload;
    },
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
  