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

    export default {
        methods: {
            async authenticate() {
                const state = randomstring.generate();
                window.localStorage.setItem('state', state);
                const keys = await CryptoService.generateKeys(
                    config.seedPhrase
                );
                const appid = config.appId;

                var scope = JSON.stringify({ doubleName: true, email: true }); // { doubleName : true, email : false}
                window.location.href = `${
                    config.botFrontEnd
                }?state=${state}&scope=${scope}&appid=${appid}&publickey=${encodeURIComponent(
                    CryptoService.getEdPkInCurve(keys.publicKey)
                )}&redirecturl=${encodeURIComponent(config.redirect_url)}`;
            },
            async redirect(state, scope, appid, publicKey, redirectUrl) {
                window.location.href = `${
                    config.botFrontEnd
                }?state=${state}&scope=${scope}&appid=${appid}&publickey=${encodeURIComponent(
                    CryptoService.getEdPkInCurve(publicKey)
                )}&redirecturl=${encodeURIComponent(redirectUrl)}`;
            },
        },
    };
</script>
<style lang="scss" scoped>
    .btn__next{
        position: absolute;
        right: 10px;
        bottom: -28px;
    }
</style>
