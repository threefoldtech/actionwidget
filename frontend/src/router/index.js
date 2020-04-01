import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
    {
        path: '/:site?/status',
        name: 'status',
        meta: {
            title: 'Status',
        },
        component: () =>
            import(/* webpackChunkName: "status" */ '../views/Status.vue'),
    },
    {
        path: '/:site?/error',
        name: 'error',
        meta: {
            title: 'Error',
        },
        component: () =>
            import(/* webpackChunkName: "error" */ '../views/Error.vue'),
    },
    {
        path: '/:site?/signup',
        name: 'signup',
        meta: {
            title: 'Signup',
        },
        component: () =>
            import(/* webpackChunkName: "signup" */ '../views/Signup.vue'),
    },
    {
        path: '/:site?/signup_step_2',
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
        path: '/:site?/callback/:userid',
        name: 'callback',
        meta: {
            title: 'Callback',
        },
        component: () =>
            import(/* webpackChunkName: "callback" */ '../views/Callback.vue'),
    },
    {
        path: '/:site?/signup_internet',
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
        path: '/:site?/signup_cyborg',
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
        path: '/:site?/intro/:userid?',
        name: 'intro',
        meta: {
            title: 'A new Internet for the planet and for humanity.',
        },
        component: () =>
            import(/* webpackChunkName: "intro" */ '../views/Intro.vue'),
    },
    {
        path: '/:site?/declaration',
        name: 'declaration',
        meta: {
            title: 'declaration',
        },
        component: () =>
            import(
                /* webpackChunkName: "declaration" */ '../views/Declaration.vue'
            ),
    },
    {
        path: '/:site?/threefold',
        name: 'threefold',
        meta: {
            title: 'Threefold',
        },
        component: () =>
            import(
                /* webpackChunkName: "threefold" */ '../views/Threefold.vue'
            ),
    },
    {
        path: '/:site?/signup_referred/',
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
        path: '/:site?/thankyou',
        name: 'thankyou',
        meta: {
            title: 'Thank you',
        },
        component: () =>
            import(/* webpackChunkName: "thankyou" */ '../views/Thankyou.vue'),
    },
    { path: '/', redirect: { name: 'intro' } },
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
});

export default router;
