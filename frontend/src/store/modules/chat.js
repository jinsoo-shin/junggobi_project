const state = {
    loading: false,
    sending: false,
    error: null,
    user: [],
    reconnect: false,
    activeRoom: null,
    rooms: [],
    users: [],
    messages: [],
    userTyping: null
}
const getters = {
    hasError: state => state.error ? true : false
}
const mutations = {
  
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
