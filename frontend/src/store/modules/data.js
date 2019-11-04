import api from '../../api'

const state = {
  items : [],
  favoriteItems : [],
  index : 0,
  valueMaxMin : [],
  chart : [],
}
const getters = {
  getFavoriteItems(state) {
    return state.favoriteItems;
  },
  getItems(state) {
    return state.items;
  },
  getCheapCost(state) {
    return state.cheapCost;
  },
  getExpenCost(state) {
    return state.expenCost;
  },
}
const mutations = {
  setAddFavoriteItems(state, payload) {
    state.favoriteItems[state.favoriteItems.length] = payload;
  },
  setDeleteFavoriteItems(state,payload) {
    for(var i=0; i<state.favoriteItems.length; i++){
      if(state.favoriteItems[i]._id === payload){
        state.favoriteItems.splice(i, 1);
        break;
      }
    }
  },
  setRangeItems(state, payload) {
    var min = payload[0];
    var max = payload[1];
    var arr = state.items;
    for(var i=0; i<arr.length; i++){
      if(min<=arr[i].price){
        console.log(arr[i].price)
        break;
      }
    }
  },
  // checkExpenCost(state, list) {
  //   var arr = list
  //   var len = arr.length, max = -Infinity;
  //   while (len--) {
  //     if (arr[len].price > max) {
  //       max = arr[len].price;
  //     }
  //   }
  //   state.expenCost = max;
  // },
  // checkCheapCost(state, list) {
  //   var arr = list
  //   var len = arr.length, min = Infinity;
  //   while (len--) {
  //     if (arr[len].price < min) {
  //       min = arr[len].price;
  //     }
  //   }
  //   state.cheapCost = min;
  // },
  setValueMaxMin(state, payload) {
    state.valueMaxMin = payload
  }
}
const actions = {
    async test1() {
      const resp = await api.test()
      state.items = resp.data
      return state.items
    },
    async searchById(state, payload) {
      const resp = await api.searchById(payload)
      state.items = resp.data.hits.hits
      state.chart = resp.data.aggregations
      console.log(state.chart)
      return state.items
    }
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}
