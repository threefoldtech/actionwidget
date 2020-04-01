import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
    { path: '/', redirect: { name: 'signup_internet' } },
    {
        path: '/signup',
        name: 'signup',
        meta: {
            title: 'Signup',
        },
        component: () =>
            import(/* webpackChunkName: "signup" */ '../views/Signup.vue'),
    },
    {
        path: '/signup_step_2',
        name: 'signup_step_2',
        meta: {
            title: 'Signup',
        },
        component: () =>
            import(
                /* webpackChunkName: "signup_step_2" */ '../views/signup/Step2.vue'
            ),
    },
    {
        path: '/callback/:userid',
        name: 'callback',
        meta: {
            title: 'Callback',
        },
        component: () =>
            import(/* webpackChunkName: "callback" */ '../views/Callback.vue'),
    },
    {
        path: '/signup_internet',
        name: 'signup_internet',
        meta: {
            title: 'Signup',
        },
        component: () =>
            import(
                /* webpackChunkName: "signup_internet" */ '../views/signup/Internet.vue'
            ),
    },
    {
        path: '/signup_cyborg',
        name: 'signup_cyborg',
        meta: {
            title: 'Signup',
        },
        component: () =>
            import(
                /* webpackChunkName: "signup_cyborg" */ '../views/signup/Cyborg.vue'
            ),
    },
    {
        path: '/signup_referred',
        name: 'signup_referred',
        meta: {
            title: 'Signup',
        },
        component: () =>
            import(
                /* webpackChunkName: "signup_referred" */ '../views/signup/Referred.vue'
            ),
    },
    {
        path: '/thankyou',
        name: 'thankyou',
        meta: {
            title: 'Thank you',
        },
        component: () =>
            import(/* webpackChunkName: "thankyou" */ '../views/Thankyou.vue'),
    },
    {
        path: '/status',
        name: 'status',
        meta: {
            title: 'Status',
        },
        component: () =>
            import(/* webpackChunkName: "status" */ '../views/Status.vue'),
    },
    {
        path: '/error',
        name: 'error',
        meta: {
            title: 'Error',
        },
        component: () =>
            import(/* webpackChunkName: "error" */ '../views/Error.vue'),
    },    
    {
        path: '/intro',
        name: 'intro',
        meta: {
            title: 'The need for a more responsible Internet.',
        },
        component: () =>
            import(/* webpackChunkName: "error" */ '../views/intro.vue'),
    },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
