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

                window.location.href = `${
                    config.botFrontEnd
                }?state=${state}&appid=${appid}&publickey=${encodeURIComponent(
                    CryptoService.getEdPkInCurve(keys.publicKey)
                )}&redirecturl=${encodeURIComponent(config.redirect_url)}`;
            },
        },
    };
</script>
