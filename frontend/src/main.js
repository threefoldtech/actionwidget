import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import vuetify from './plugins/vuetify';
import Clipboard from 'v-clipboard';
import '@fortawesome/fontawesome-free/css/all.css';
import './styles/style.css';
import Progress from './components/Progress';

Vue.config.productionTip = false;

Vue.component('Progress', Progress);
new Vue({
    router,
    store,
    vuetify,
    Clipboard,
    render: h => h(App),
}).$mount('#app');
