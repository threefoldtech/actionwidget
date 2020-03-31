<template>
    <div class="signup_referred">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class=" mt-5 py-6 mx-auto" max-width="800" tile>
                    <span></span>
                    <v-btn @click="authenticate"
                        >I have installed the app</v-btn
                    >
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
            };
        },
        mounted() {
            if (!this.$route.query.userid) {
                router.push('error');
            }
            this.userid = this.$route.query.userid;
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
<style lang="scss" scoped>
    .btn__next {
        position: absolute;
        right: 10px;
        bottom: -28px;
    }
</style>
