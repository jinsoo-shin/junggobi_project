import api from '../../api'

const state = {
    items: [],
    favoriteItems: [],
    index: 0,
    articles: [],
}
const getters = {
    getFavoriteItems(state) {
        return state.favoriteItems;
    },
    getItems(state) {
        return state.items;
    },
    getBlogPosts(state) {
        return state.articles;
    }
}
const mutations = {
    setAddFavoriteItems(state, payload) {
        state.favoriteItems[state.favoriteItems.length] = payload;
    },
    setDeleteFavoriteItems(state, payload) {
        for (var i = 0; i < state.favoriteItems.length; i++) {
            if (state.favoriteItems[i].id === payload) {
                state.favoriteItems.splice(i, 1);
                break;
            }
        }
    },
    checkExpenCost(state, list) {
        var arr = list
        var len = arr.length,
            max = -Infinity;
        while (len--) {
            if (arr[len].price > max) {
                max = arr[len].price;
            }
        }
        // console.log(state.expenCost)
        state.expenCost = max;
    },
    checkCheapCost(state, list) {
        var arr = list
            // console.log(arr)
        var len = arr.length,
            min = Infinity;
        while (len--) {
            if (arr[len].price < min) {
                min = arr[len].price;
            }
        }
        state.cheapCost = min;
    }
}
const actions = {
    async test1() {
        const resp = await api.test()
        state.items = resp.data
        return state.items
    },
    async getBlogPost() {
        const resp = await api.getBlogpost()
        state.articles = resp.data
        return state.articles
    },
}
export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}