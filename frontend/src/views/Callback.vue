<template>
    <div>
        callback
    </div>
</template>

<script>
    import config from '../../public/config';
    import cryptoService from '../services/CryptoService';
    import threebotService from '../services/threebotService';
    import router from '../router';
    import axios from 'axios';
    import { mapMutations } from 'vuex';

    export default {
        name: 'callback',
        data() {
            return {
                username: null,
                verified: false,
                error: null,
            };
        },
        async mounted() {
            if (!this.$route.params.userid) {
                router.push('error');
            }

            let url = new URL(window.location.href);

            let error = url.searchParams.get('error');

            if (error) {
                return;
            }

            let signedAttemptObject = JSON.parse(
                url.searchParams.get('signedAttempt')
            );

            let user = signedAttemptObject['doubleName'];
            let userPublicKey = (await threebotService.getUserData(user)).data
                .publicKey;

            let verifiedSignedAttempt;

            try {
                const utf8ArrayToStr = (() => {
                    const charCache = new Array(128);
                    const charFromCodePt =
                        String.fromCodePoint || String.fromCharCode;
                    const result = [];

                    return array => {
                        let codePt, byte1;
                        const buffLen = array.length;

                        result.length = 0;

                        for (let i = 0; i < buffLen; ) {
                            byte1 = array[i++];

                            if (byte1 <= 0x7f) {
                                codePt = byte1;
                            } else if (byte1 <= 0xdf) {
                                codePt =
                                    ((byte1 & 0x1f) << 6) | (array[i++] & 0x3f);
                            } else if (byte1 <= 0xef) {
                                codePt =
                                    ((byte1 & 0x0f) << 12) |
                                    ((array[i++] & 0x3f) << 6) |
                                    (array[i++] & 0x3f);
                            } else if (String.fromCodePoint) {
                                codePt =
                                    ((byte1 & 0x07) << 18) |
                                    ((array[i++] & 0x3f) << 12) |
                                    ((array[i++] & 0x3f) << 6) |
                                    (array[i++] & 0x3f);
                            } else {
                                codePt = 63;
                                i += 3;
                            }

                            result.push(
                                charCache[codePt] ||
                                    (charCache[codePt] = charFromCodePt(codePt))
                            );
                        }

                        return result.join('');
                    };
                })();

                verifiedSignedAttempt = JSON.parse(
                    utf8ArrayToStr(
                        await cryptoService.validateSignedAttempt(
                            signedAttemptObject['signedAttempt'],
                            userPublicKey
                        )
                    )
                );

                if (!verifiedSignedAttempt) {
                    return;
                }

                let state = window.localStorage.getItem('state');

                if (verifiedSignedAttempt['signedState'] !== state) {
                    return;
                }

                if (verifiedSignedAttempt['doubleName'] !== user) {
                    return;
                }
            } catch (e) {
                return;
            }

            let encryptedData = verifiedSignedAttempt['data'];

            // Keys from the third party app itself, or a temp keyset if it is a front-end only third party app.
            let keys = await cryptoService.generateKeys(config.seedPhrase);

            let decryptedData = JSON.parse(
                await cryptoService.decrypt(
                    encryptedData.ciphertext,
                    encryptedData.nonce,
                    keys.privateKey,
                    userPublicKey
                )
            );

            decryptedData['name'] = user;

            // SEI = Signed Email Identifier, this is used to link the email to the doubleName and verify it.
            if (!decryptedData.email || !decryptedData.email.sei) {
                return;
            }
            // To verify the SEI, you could use the function implemented by openKYC or verify it yourself using openKYC his publicKey.
            let seiVerified = await threebotService.verifySignedEmailIdentifier(
                decryptedData.email.sei
            );

            if (!seiVerified || seiVerified.status !== 200) {
                return;
            }
            // @todo: error handling
            axios.post('/api/referral_done', {
                referral_3bot_name: seiVerified.data.identifier,
                user_id: this.$route.params.userid,
            });
            this.setEmail(seiVerified.data.email);
            this.setUserId(this.$route.params.userid);

            //@todo use callback
            await router.push({ name: 'signup' });
        },
        methods: {
            ...mapMutations(['setEmail', 'setUserId']),
        },
    };
</script>

<style lang="scss" scoped></style>
