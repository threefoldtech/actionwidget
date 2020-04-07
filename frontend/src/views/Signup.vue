<template>
    <div class="signup">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <Progress step="3" />
                    <v-form
                        class="ma-5"
                        lazy-validation
                        ref="form"
                        v-model="valid"
                    >
                        <v-checkbox
                            v-model="reserve_3bot"
                            label="Reserve my digital twin name (unique new internet ID)"
                        />
                        <v-text-field
                            v-if="reserve_3bot"
                            v-model="threeBotName"
                            validate-on-blur
                            :rules="threeBotNameRules"
                            label="Double name"
                            required
                            persistent-hint
                        ></v-text-field>
                        <p v-if="doubleNameExist" class="red--text" >This double name is already in use. Please choose another double name.</p>
                        <v-checkbox
                            v-model="internetCapacity"
                            label="I want to learn more about how I can provide Internet capacity to people around me"
                        />
                        <v-checkbox
                            v-model="ITSolutions"
                            label="I want to learn more about how I can deploy my own IT solutions on this new internet"
                        />
                        <v-text-field
                            v-model="userName"
                            validate-on-blur
                            label="Your name"
                            :rules="userNameRules"
                            required
                            persistent-hint
                        ></v-text-field>
                        <v-text-field
                            v-model="signupEmail"
                            :rules="emailRules"
                            label="E-mail"
                            required
                            validate-on-blur
                        ></v-text-field>

                        <v-checkbox
                            v-model="canSendEmail"
                            label="I agree to being kept informed about this new Internet by email."
                            :rules="[v => !!v || 'You must agree to continue!']"
                        />
                        <p> ( Your data is safe with us, see our privacy policy <a href="https://docs.google.com/document/d/16i6M2Bkxh0o5kbDOuBCnErPJ_OKM1uLkgPWJwexZ9lQ/edit?usp=sharing" target="_blank">here</a> )</p>
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
                        <v-btn
                            class="btn__previous"
                            elevation="2"
                            fab
                            mini
                            to="acknowledgements"
                            color="#1072ba"
                            dark
                            ><v-icon>fas fa-chevron-left</v-icon></v-btn
                        >
                    </v-form>
                </v-card>
            </v-row>
        </v-container>
    </div>
</template>
<script>
    import router from '../router';
    import axios from 'axios';

    export default {
        data: () => ({
            valid: true,
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            threeBotNameRules: [
                v => v.length <= 40 || 'Name must be less than 40 characters',
                v =>
                    /^[a-zA-Z0-9]+\.[a-zA-Z0-9]+$/.test(v) || 
                    'Please use alphanumerics charachters only (0-9 and a-z). Use a dot (.) in your double name. ',
                v => v.indexOf('.3bot') === -1 || '.3bot suffix is not allowed',
            ],
            userNameRules: [
                v => !!v || 'Your name is required',
                v => v.length <= 40 || 'Name must be less than 40 characters',
                v =>
                    /^[a-zA-Z0-9 ]+$/.test(v) ||
                    'Please use alphanumerics charachters only (0-9 and a-z)',

                //v => /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/.test(v) || 'Name must be valid',
            ],
            loading: false,
            doubleNameExist: false,
        }),
        computed: {
            signupEmail: {
                get() {
                    return this.$store.state.signupForm.signupEmail;
                },
                set(value) {
                    this.$store.commit('updateSignupEmail', value);
                },
            },
            userName: {
                get() {
                    return this.$store.state.signupForm.userName;
                },
                set(value) {
                    this.$store.commit('updateUserName', value);
                },
            },
            threeBotName: {
                get() {
                    return this.$store.state.signupForm.threeBotName;
                },
                set(value) {
                    this.$store.commit('updateThreeBotName', value);
                },
            },
            reserve_3bot: {
                get() {
                    return this.$store.state.signupForm.reserve_3bot;
                },
                set(value) {
                    this.$store.commit('updateReserve3bot', value);
                },
            },
            ITSolutions: {
                get() {
                    return this.$store.state.signupForm.ITSolutions;
                },
                set(value) {
                    this.$store.commit('updateITSolutions', value);
                },
            },
            internetCapacity: {
                get() {
                    return this.$store.state.signupForm.internetCapacity;
                },
                set(value) {
                    this.$store.commit('updateInternetCapacity', value);
                },
            },
            canSendEmail: {
                get() {
                    return this.$store.state.signupForm.canSendEmail;
                },
                set(value) {
                    this.$store.commit('updateCanSendEmail', value);
                },
            },
        },
        methods: {
            async validateAndSubmit() {
                if (!this.$refs.form.validate()) {
                    return;
                }
                this.loading = true;
                try{
                    const response = await axios.put(`/api/user`, {
                        email_address: this.signupEmail,
                        name: this.userName,
                        double_name:
                            this.reserve_3bot === true ? this.threeBotName : null,
                        internet_capacity: this.internetCapacity,
                        deploy_solutions: this.ITSolutions,
                    });
                    if (!response.data.success) {
                        await router.push('error');
                        return;
                    }
                }catch(e){
                    if(e.response.status === 409){
                        this.reserve_3bot = true;
                        return
                    }
                }
                await router.push('thankyou');
            },
        },
    };
</script>
