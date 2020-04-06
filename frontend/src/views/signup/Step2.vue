<template>
    <div class="signup__step2">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <Progress step="5" />
                    <v-form
                        class="ma-5"
                        lazy-validation
                        ref="form"
                        v-model="valid"
                    >
                        <v-checkbox
                            v-model="referral"
                            label="Do you want to refer us to others and be part of our referral program."
                        />
                        <v-checkbox
                            v-model="currencies"
                            label="Are you interested to know more about our related digital currencies?"
                        />
                        <v-btn
                            :disabled="!valid"
                            :loading="loading"
                            @click="validateAndSubmit"
                            class="btn__next white--text"
                            fab
                            mini
                            color="#1072ba"
                        >
                            <v-icon class="ml-1">fas fa-chevron-right</v-icon>
                        </v-btn>
                    </v-form>
                </v-card>
            </v-row>
        </v-container>
    </div>
</template>

<script>
    import axios from 'axios';
    import router from '../../router';
    import { mapGetters } from 'vuex';

    export default {
        name: 'Step2',
        mounted() {
            if (!this.$store.getters.referrerToken) {
                router.push('error');
            }
        },
        computed: {
            ...mapGetters(['userId', 'referrerToken']),
        },
        methods: {
            async validateAndSubmit() {
                if (!this.$refs.form.validate()) {
                    return;
                }
                this.loading = true;
                await axios.post(`/api/set_referral_and_currency`, {
                    user_referrer_token: this.referrerToken,
                    referral: this.referral,
                    currencies: this.currencies,
                });

                router.push('thankyou');
            },
        },
        data() {
            return {
                valid: true,
                referral: false,
                currencies: false,
                loading: false,
            };
        },
    };
</script>
