import { apiService } from '@/api'

const namespaced = true;

const state = {
    user: {},
    isLoggedIn: false
};

const getters = {
    isLoggedIn: state => state.isLoggedIn,
    user: state => state.user
};
    
console.log("lalala")

const actions = {
    async loginUser({ dispatch }, user) {
        console.log("entrooooo")
        await apiService.post('/auth/login_jwt', user)
        console.log("entrooooo 222")
        await dispatch('fetchUser')
        console.log("entrooooo 333")
    },
    async fetchUser({ commit }) {
        await apiService.get('/auth/user_jwt')
            .then(({ data }) => commit('setUser', data))
    },
    async logoutUser({ commit }) {
        await apiService.get('/auth/logout_jwt');
        commit('logoutUserState');
    }
};

const mutations = {
    setUser(state, user) {
        state.isLoggedIn = true;
        state.user = user;
    },
    logoutUserState(state) {
        state.isLoggedIn = false;
        state.user = {};
    }
};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations
};