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
    getLoading(state){
        return state.loading
    },
    getSending(state){
        return state.sending
    },
    getError(state){
        return state.error
    },
    getUser(state){
        return state.user
    },
    getReconnect(state){
        return state.reconnect
    },
    getActiveRoom(state){
        return state.activeRoom
    },
    getRooms(state){
        return state.rooms
    },
    getUsers(state){
        return state.users
    },
    getMessages(state){
        return state.messages
    },
    getUserTyping(state){
        return state.userTyping
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
