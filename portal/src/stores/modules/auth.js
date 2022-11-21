import { getApiService } from '@/api'

const namespaced = true;

const state = {
    user: {},
    token:null,
    isLoggedIn: false,
    cuotas:{},
    disciplinas:{},
    disciplinasAsociado: {}
};

const getters = {
    isLoggedIn: state => state.isLoggedIn,
    user: state => state.user,
    cuotas: state => state.cuotas,
    disciplinas: state => state.disciplinas,
    carnet: state => state.carnet,
    disciplinasAsociado: state => state.disciplinasAsociado,
};

const actions = {
    async loginUser({ dispatch }, user) {
        await getApiService().service.post('/auth', user).then((response)=>{
             localStorage.setItem( 'token', JSON.stringify(response.data.token) );
        }) //services para sin autenticacion
        await dispatch('fetchUser')
    },
    async fetchUser({ commit }) {
        await getApiService().servicesAuth.get('/me/profile') // para las autenticaciones
            .then(({ data }) => commit('setUser', data))
    },
    async logoutUser({ commit }) {
        //await apiService.get('/auth/logout_jwt');
        commit('logoutUserState');
    },
    async cuotasUsuario({ commit }) {
        await getApiService().servicesAuth.get('/me/payments').then((response)=>{
            commit('setCuotas',response.data)
        });
    },
    async disciplinasClub({ commit }) {
        await getApiService().service.get('/club/disciplines').then((response)=>{
            commit('setDisciplinas',response.data)
        });
    },
    async carnetAsociado({ commit }) {
        await getApiService().servicesAuth.get('/me/license').then((response)=>{
            console.log(response.data);
            commit('setCarnet',response.data);
        });
    },
    async disciplinasAsociado({ commit }) {
        await getApiService().servicesAuth.get('/me/disciplines').then((response)=>{
            commit('setDisciplinasAsociado',response.data)
        });
    },
};

const mutations = {
    setUser(state, user) {
        state.isLoggedIn = true;
        state.user = user;
    },
    logoutUserState(state) {
        state.isLoggedIn = false;
        state.user = {};
    },
    setCuotas(state,cuota) {
        state.cuotas = cuota;
    },
    setDisciplinas(state,disciplinas) {
        state.disciplinas = disciplinas;
    },
    setCarnet(state,carnet) {
        state.carnet = carnet;
    },
    setDisciplinasAsociado(state,disciplinasAsociado) {
        state.disciplinasAsociado = disciplinasAsociado;
    },

};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations
};