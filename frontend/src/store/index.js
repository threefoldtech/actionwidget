import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
    state: {
        email: null,
        userId: null,
        referrerToken: null,
    },
    mutations: {
        setEmail(state, email) {
            state.email = email;
        },
        setUserId(state, userId) {
            state.userId = userId;
        },
        setReferrerToken(state, referrerToken) {
            state.referrerToken = referrerToken;
        },
    },
    getters: {
        email: state => state.email,
        userId: state => state.userId,
        referrerToken: state => state.referrerToken,
    },
    modules: {},
});
