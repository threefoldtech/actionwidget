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
        path: '/signup_step2',
        name: 'signup_step_2',
        component: () =>
            import(
                /* webpackChunkName: "signup_step_2" */ '../views/signup/Step2.vue'
            ),
    },
    {
        path: '/callback/:userid',
        name: 'callback',
        component: () =>
            import(/* webpackChunkName: "callback" */ '../views/Callback.vue'),
    },
    {
        path: '/signup_internet',
        name: 'signup',
        component: () =>
            import(
                /* webpackChunkName: "signup_internet" */ '../views/signup/Internet.vue'
            ),
    },
    {
        path: '/signup_cyborg',
        name: 'signup',
        component: () =>
            import(
                /* webpackChunkName: "signup_cyborg" */ '../views/signup/Cyborg.vue'
            ),
    },
    {
        path: '/signup_referred',
        name: 'signup',
        component: () =>
            import(
                /* webpackChunkName: "signup_referred" */ '../views/signup/Referred.vue'
            ),
    },
    {
        path: '/error',
        name: 'error',
        component: () =>
            import(/* webpackChunkName: "error" */ '../views/Error.vue'),
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
