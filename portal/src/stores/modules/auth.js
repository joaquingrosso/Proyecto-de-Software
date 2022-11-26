import { getApiService } from '@/api'

const namespaced = true;

const state = {
    user: {}, //meterlo en el storage
    token:null,
    isLoggedIn: false,//meterlo en el storage
    cuotasImpagas:{},
    disciplinas:{},
    disciplinasAsociado: {},
    pago:{},
    statsAsocXMes:{},
    statsAsocXDisc:{},
    statsMorosAlDia:{},
    pagosRealizados:{},
    contacto:{}
};

const getters = {
    isLoggedIn: state => state.isLoggedIn,
    user: state => state.user,
    cuotasImpagas: state => state.cuotasImpagas,
    disciplinas: state => state.disciplinas,
    carnet: state => state.carnet,
    disciplinasAsociado: state => state.disciplinasAsociado,
    pago: state => state.pago,
    statsAsocXMes: state => state.statsAsocXMes,
    statsAsocXDisc: state => state.statsAsocXDisc,
    statsMorosAlDia: state => state.statsMorosAlDia,
    pagosRealizados: state => state.pagosRealizados,
    contacto: state => state.contacto,
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
    async cuotasUsuarioImpagas({ commit }) {
        await getApiService().servicesAuth.get('/me/mostrar_cuotas_impagas').then((response)=>{
            commit('setCuotasImpagas',response.data)
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
    async pagarCuotaAsociado({ commit },pago) {
        await getApiService().servicesAuth.post('/me/payments', pago).then((response)=>{ 
            commit('setPago',response.data)
        })
    },
    async verCuotaAsociado({ commit }) {
        await getApiService().servicesAuth.get('/me/payments').then((response)=>{ 
            console.log(response.data);
            commit('setPagosRealizados',response.data)
        })
    },
    async asociadosInscriptosPorMes({ commit }) {
        await getApiService().service.get('/stats/asociado_por_año').then((response)=>{ 
            commit('setAsocXmes',response.data)
        })
    },
    async asociadosInscriptosPorDisciplina({ commit }) {
        await getApiService().service.get('/stats/asociado_por_disciplinas').then((response)=>{ 
            commit('setAsocXDisc',response.data)
        })
    },
    async asociadosMorososAlDia({ commit }) {
        await getApiService().service.get('/stats/morosos_al_dia').then((response)=>{ 
            commit('setAsocMxAD',response.data)
        })
    },
    establecerStateLoggedIn_User({ commit }){
        commit('setUser', localStorage.getItem('user'))
    },
    async infoContacto({ commit }) {
        await getApiService().service.get('/club/info').then((response)=>{ 
            commit('setContacto',response.data)
        })
    },

};

const mutations = {
    setUser(state, user) {
        state.isLoggedIn = true;
        state.user = user;
        localStorage.setItem("user", state.user);        
        localStorage.setItem("isLoggedIn", state.isLoggedIn);
    },
    logoutUserState(state) {
        state.isLoggedIn = false;
        state.user = {};
    },
    setCuotasImpagas(state,cuota) {
        state.cuotasImpagas = cuota;
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
    setPago(state,pago){
        state.pago = pago;
    },
    setAsocXmes(state,asocXmes){
        state.statsAsocXMes = asocXmes;
    },
    setAsocXDisc(state,asocXdisc){
        state.statsAsocXDisc = asocXdisc;
    },
    setAsocMxAD(state,asocMxAD){        
        state.statsMorosAlDia = asocMxAD;
    },
    setPagosRealizados(state,pagos){        
        state.pagosRealizados = pagos;
    },
    setContacto(state,contacto){
        state.contacto = contacto;
    }


};

export default {
    namespaced,
    state,
    getters,
    actions,
    mutations
};