import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import Clipboard from 'v-clipboard';
import '@fortawesome/fontawesome-free/css/all.css';
import './styles/style.css';

Vue.config.productionTip = false;

new Vue({
    router,
    store,
    vuetify,
    Clipboard,
    render: h => h(App),
}).$mount('#app');
