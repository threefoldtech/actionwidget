<template>
    <v-app>
        <link
            href="https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap"
            rel="stylesheet"
        />

        <v-app-bar app color="white">
            <div class="d-flex align-center">
                <v-img src="./assets/logo.png" height="45" width="200"></v-img>
            </div>
        </v-app-bar>
        <v-content>
            <div id="app" class="back">
                <h1 class="text-center mr-6 pt-6">
                    {{ $route.meta.title || $route.name || 'Referrer' }}
                </h1>
                <router-view></router-view>
            </div>
        </v-content>
    </v-app>
</template>
