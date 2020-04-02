<template>
    <div class="signup_referred">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" width="800" tile>
                    <Progress step="4"/>
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <p>
                                    Please install the install 3bot Connect app
                                </p>
                            </v-col>
                            <v-col cols="12" sm="6">
                                <a
                                    href="https://play.google.com/store/apps/details?id=org.jimber.threebotlogin"
                                    target="_blank"
                                >
                                    <v-img
                                        :src="
                                            require('@/assets/googleplay.png')
                                        "
                                        aspect-ratio="1"
                                        height="60"
                                        width="210"
                                    ></v-img>
                                </a>
                            </v-col>
                            <v-col cols="12" sm="6">
                                <a
                                    href="https://apps.apple.com/be/app/3bot-login/id1459845885?l=nl"
                                    target="_blank"
                                >
                                    <v-img
                                        :src="
                                            require('@/assets/app-store-icon.png')
                                        "
                                        aspect-ratio="1"
                                        height="60"
                                        width="210"
                                    ></v-img>
                                </a>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="12" sm="6">
                                <v-checkbox
                                    v-model="installed"
                                    :label="
                                        `I've installed the 3Bot connect app`
                                    "
                                ></v-checkbox>
                            </v-col>
                        </v-row>
                        <v-row align="center" justify="center">
                            <v-col cols="12" sm="6">
                                <v-btn
                                    @click="authenticate"
                                    v-bind:disabled="!installed"
                                    color="#1072ba"
                                    class="white--text"
                                    >Login</v-btn
                                >
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card>
            </v-row>
        </v-container>
    </div>
</template>

<script>
    import config from '../../../public/config';
    import CryptoService from '../../services/CryptoService';
    import randomstring from 'randomstring';
    import router from '../../router';

    export default {
        data() {
            return {
                userid: null,
                installed: false,
            };
        },
        mounted() {
            if (!this.$route.params.userid) {
                router.push('error');
            }
            this.userid = this.$route.params.userid;
        },
        methods: {
            async authenticate() {
                const state = randomstring.generate();
                window.localStorage.setItem('state', state);
                const keys = await CryptoService.generateKeys(
                    config.seedPhrase
                );
                const appid = config.appId;

                const scope = JSON.stringify({ doubleName: true, email: true }); // { doubleName : true, email : false}
                const redirectUrl = encodeURIComponent(
                    `${config.redirect_url}/${this.userid}`
                );
                const publicKey = encodeURIComponent(
                    CryptoService.getEdPkInCurve(keys.publicKey)
                );
                window.location.href = `${config.botFrontEnd}?state=${state}&scope=${scope}&appid=${appid}&publickey=${publicKey}&redirecturl=${redirectUrl}`;
            },
        },
    };
</script>
