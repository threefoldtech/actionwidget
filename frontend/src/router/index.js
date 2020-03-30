import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
    {
        path: '/signup',
        name: 'signup',
        component: () =>
            import(/* webpackChunkName: "signup" */ '../views/Signup.vue'),
    },
    {
        path: '/callback',
        name: 'callback',
        component: () =>
            import(/* webpackChunkName: "callback" */ '../views/Callback.vue'),
    },
    {
        path: '/signup_internet',
        name: 'signup_internet',
        component: () =>
            import(
                /* webpackChunkName: "signup_internet" */ '../views/signup/Internet.vue'
            ),
    },
    {
        path: '/signup_cyborg',
        name: 'signup_cyborg',
        component: () =>
            import(
                /* webpackChunkName: "signup_cyborg" */ '../views/signup/Cyborg.vue'
            ),
    },
    {
        path: '/signup_referred',
        name: 'signup_referred',
        component: () =>
            import(
                /* webpackChunkName: "signup_referred" */ '../views/signup/Referred.vue'
            ),
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
