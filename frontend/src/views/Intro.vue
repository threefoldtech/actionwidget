<template>
    <div class="intro__page">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <Progress step="1" />
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <div>
                                    <h3 class="mb-2">
                                        The need for a more responsible
                                        Internet.
                                    </h3>
                                    <p>
                                        We use the Internet every day, yet most
                                        of us don’t know, or think, too much
                                        about it.
                                    </p>
                                    <p>
                                        Despite serving our daily needs rather
                                        well until today, the Internet is now
                                        reaching a critical point. Among the
                                        issues it is facing, the Internet now
                                        struggles with global data demands, and
                                        the overly-complex global architecture
                                        behind it is centralized, making it
                                        inefficient and unsustainable.
                                    </p>
                                    <p>
                                        Did you know that about half of the
                                        world’s population remains unconnected
                                        to the Internet despite being a human
                                        right? Do you find it fair that large
                                        multinational corporations profit off of
                                        our user data? Why don’t we talk more
                                        about the fact that the Internet
                                        consumes between 5% and 10% of global
                                        energy?
                                    </p>
                                    <p>
                                        A new Internet is needed, for both our
                                        planet and for humanity. One that
                                        addresses these challenges.
                                    </p>
                                    <p>
                                        The foundation for this new Internet
                                        already exists. Follow the next steps to
                                        learn more.
                                    </p>
                                </div>
                            </v-col>
                        </v-row>
                    </v-container>

                    <v-btn
                        class="btn__next"
                        elevation="3"
                        fab
                        mini
                        :to="{
                            name: 'declaration',
                            params: { ...this.$route.params },
                        }"
                        color="#1072ba"
                        dark
                        ><v-icon class="ml-1"
                            >fas fa-chevron-right</v-icon
                        ></v-btn
                    >
                </v-card>
            </v-row>
            <v-row align="center" justify="center"></v-row>
        </v-container>
    </div>
</template>
<script>
    import { mapMutations } from 'vuex';

    export default {
        name: 'intro',
        methods: {
            ...mapMutations(['setUserId']),
        },
    };
</script>
