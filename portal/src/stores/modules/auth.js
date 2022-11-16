import { apiService } from '@/api'

const namespaced = true;

const state = {
    user: {},
    token:null,
    isLoggedIn: false
};

const getters = {
    isLoggedIn: state => state.isLoggedIn,
    user: state => state.user
};

const actions = {
    async loginUser({ dispatch }, user) {
        console.log("entro en el auth")
        await apiService.service.post('/auth', user).then((response)=>{
             localStorage.setItem( 'token', JSON.stringify(response.data.token) );
        }) //services para sin autenticacion
        await dispatch('fetchUser')
    },
    async fetchUser({ commit }) {
        console.log("entro al fetchUser")
        await apiService.servicesAuth.get('/me/profile') // para las autenticaciones
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