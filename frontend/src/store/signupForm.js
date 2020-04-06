export default {
    state: {
        signupEmail: '',
        userName: '',
        threeBotName: '',
        reserve_3bot: false,
        ITSolutions: false,
        internetCapacity: false,
        canSendEmail: false,
    },
    mutations: {
        updateSignupEmail(state, value) {
            state.signupEmail = value;
        },
        updateUserName(state, value) {
            state.userName = value;
        },
        updateThreeBotName(state, value) {
            state.threeBotName = value;
        },
        updateReserve3bot(state, value) {
            state.reserve_3bot = value;
        },
        updateITSolutions(state, value) {
            state.ITSolutions = value;
        },
        updateInternetCapacity(state, value) {
            state.internetCapacity = value;
        },
        updateCanSendEmail(state, value) {
            state.canSendEmail = value;
        },
    },
    getters: {},
};
