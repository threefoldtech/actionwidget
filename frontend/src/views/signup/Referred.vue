<template>
    <div class="signup_referred">
        <span></span>
        <v-btn @click="authenticate">I have installed the app</v-btn>
    </div>
</template>

<script>
    // import config from '../../../public/config';
    // const randomstring = require('randomstring')
    //
    // import CryptoService from '../../services/CryptoService'

    export default {
        methods: {
            async authenticate() {
                // const state = randomstring.generate();
                // window.localStorage.setItem('state', state);
                // const keys = await CryptoService.generateKeys(
                //     config.seedPhrase
                // );
                // const appid = config.appId;
                //
                // window.location.href = `${
                //     config.botFrontEnd
                // }?state=${state}&appid=${appid}&publickey=${encodeURIComponent(
                //     CryptoService.getEdPkInCurve(keys.publicKey)
                // )}&redirecturl=${encodeURIComponent(config.redirect_url)}`;
            },
        },
    };
</script>
