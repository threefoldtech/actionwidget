<template>
    <v-app>
        <v-app-bar app color="primary" dark>
            <div class="d-flex align-center">
                <h1 class="title text-uppercase">
                    {{ $route.meta.title || $route.name || 'Referrer' }}
                </h1>
            </div>
        </v-app-bar>
        <v-content>
            <router-view></router-view>
        </v-content>
    </v-app>
</template>
