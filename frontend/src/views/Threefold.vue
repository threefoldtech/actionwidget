<template>
    <div class="intro__page">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <Progress step="2" />
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <h3>A new Internet for the planet and for humanity</h3> <br> 
                                <p>
                                    A new Internet is here. One that is truly sustainable, accessible, and empowers its users.
                                </p>
                                <p>The ThreeFold Network brings a green and responsible peer-to-peer Internet that is available everywhere and owned by everyone – across geographical and cultural borders. An Internet that empowers people to
                                be digitally independent and provide equal chances to learn, partake, and succeed.
                                </p>
                                <p>What changes with the ThreeFold Network?</p>
                                <ul class="ml-4">
                                    <li>90% more sustainable: fully decentralized and uses the most sustainable hardwares and softwares</li>
                                    <li>100% peer-to-peer: everyone owns their data and experiences. No centralized institution or governance</li>
                                    <li>3,000% more affordable: access Internet services for a fraction of today’s cost. The Internet should be available and affordable to all</li>
                                    <li>Switch from a centralized and app centric digital world to one with you in the center</li>
                                </ul>
                            </v-col>
                        </v-row>
                        <v-row >
                            <v-col cols="12" sm="12">
                                    <h3>Visit us</h3>
                            </v-col>
                            <v-col cols="12" sm="6">
                                    <a :href="'https://threefold.io'" target="_blank">
                                        <v-col cols="12" sm="6">
                                                <v-img src="../assets/logo.png" height="45" width="150"></v-img> 
                                        </v-col>
                                    </a> 
                            </v-col>
                            <v-col cols="12" sm="6" class="mt-4">
                                    <a :href="'https://forum.threefold.io/'" target="_blank"><h4>Threefold forums</h4></a>
                            </v-col>                            
                        </v-row>
                    </v-container>
                    <v-btn
                        class="btn__previous"
                        elevation="3"
                        fab
                        mini
                        to="intro"
                        color="#1072ba"
                        dark
                        ><v-icon class="m-1"
                            >fas fa-chevron-left</v-icon
                        ></v-btn
                    >
                    <v-btn
                        v-if="userId"
                        class="btn__next"
                        elevation="3"
                        fab
                        mini
                        :to="{
                            name: 'signup_referred',
                            params: {
                                userid: userId,
                                site: this.$route.params.site,
                            },
                        }"
                        color="#1072ba"
                        dark
                        ><v-icon class="ml-1"
                            >fas fa-chevron-right</v-icon
                        ></v-btn
                    >
                    <v-btn
                        v-else
                        class="btn__next"
                        elevation="3"
                        fab
                        mini
                        to="signup"
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
    import { mapGetters } from 'vuex';

    export default {
        name: 'threefold',
        computed: {
            ...mapGetters(['userId']),
        },
        mounted() {
            if (this.$route.params.userid) {
                this.setUserId(this.$route.params.userid);
            }
        },
    };
</script>
