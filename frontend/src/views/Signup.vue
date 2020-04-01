<template>
    <div class="signup">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <v-form
                        class="ma-5"
                        lazy-validation
                        ref="form"
                        v-model="valid"
                    >
                        <v-checkbox
                            v-model="reserve_3bot"
                            label="I want to reserve my digital twin"
                        />
                        <v-checkbox
                            v-model="videoconf"
                            label="I am interested to have my own video conferencing solution which allows me to communicate with everyone in the world"
                        />
                        <v-checkbox
                            v-model="social_media"
                            label="I am interested in a peer2peer alternative social media network for private & business usage"
                        />
                        <v-checkbox
                            v-model="farmer"
                            label="I am interested to learn more about become a farmer and provide internet capacity for people around me"
                        />
                        <v-checkbox
                            v-model="deploy_it"
                            label="I am interested to know more about how to deploy my own IT solutions on this new internet (maybe not)"
                        />
                        <span>I agree that</span>
                        <v-checkbox
                            v-model="gdpr"
                            label="GDPR "
                            :rules="[v => !!v || 'You must agree to continue!']"
                        />
                        <v-checkbox
                            v-model="cookies"
                            label="We are allowed to put cookies from our websites"
                            :rules="[v => !!v || 'You must agree to continue!']"
                        />
                        <v-checkbox
                            v-model="canSendEmail"
                            label="We are allowed to email them"
                            :rules="[v => !!v || 'You must agree to continue!']"
                        />
                        <v-text-field
                            v-model="signupEmail"
                            :rules="emailRules"
                            label="E-mail"
                            required
                            validate-on-blur
                            :disabled="!!email"
                        ></v-text-field>
                        <v-text-field
                            v-model="mobile"
                            :rules="mobileRules"
                            validate-on-blur
                            label="Mobile"
                            type="tel"
                            hint="optional"
                            persistent-hint
                        ></v-text-field>
                        <v-btn
                            :disabled="!valid"
                            elevation="3"
                            fab
                            mini
                            color="#1072ba"
                            class="btn__next white--text"
                            :loading="loading"
                            @click="validateAndSubmit"
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
    import router from '../router';
    import axios from 'axios';
    import { mapGetters, mapMutations } from 'vuex';

    export default {
        data: () => ({
            valid: true,
            signupEmail: '',
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            mobile: '',
            mobileRules: [
                v => {
                    if (!v) {
                        return true;
                    }
                    return (
                        /^((\+\d{1,3}(-| )?\(?\d\)?(-| )?\d{1,5})|(\(?\d{2,6}\)?))(-| )?(\d{3,4})(-| )?(\d{4})(( x| ext)\d{1,5}){0,1}$/.test(
                            v
                        ) || 'Mobile nr must be valid'
                    );
                },
            ],
            reserve_3bot: false,
            videoconf: false,
            social_media: false,
            farmer: false,
            deploy_it: false,
            canSendEmail: false,
            gdpr: false,
            cookies: false,
            loading: false,
        }),
        computed: {
            ...mapGetters(['email', 'referrerToken']),
        },
        mounted() {
            if (this.email) {
                this.signupEmail = this.email;
            }
        },
        methods: {
            ...mapMutations(['setReferrerToken']),
            async validateAndSubmit() {
                if (!this.$refs.form.validate()) {
                    return;
                }

                const email = this.email || this.signupEmail;
                this.loading = true;

                const host3botName = this.$route.params.site || '';

                const response = await axios.put(`/api/user`, {
                    mobile: this.mobile,
                    reserve_3bot: this.reserve_3bot,
                    videoconf: this.videoconf,
                    social_media: this.social_media,
                    farmer: this.farmer,
                    deploy_it: this.deploy_it,
                    gdpr: this.gdpr,
                    cookies: this.cookies,
                    email_address: email,
                    email: this.canSendEmail,
                    host_3bot_name: host3botName,
                });
                if (!response.data.success) {
                    await router.push('error');
                    return;
                }

                const referrerToken = response.data.data.user_referrer_token;

                this.setReferrerToken(referrerToken);
                await router.push('signup_step_2');
            },
        },
    };
</script>
