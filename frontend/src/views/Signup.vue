<template>
    <div class="signup">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <Progress step="3"/>
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
                            suffix=".3bot"
                            label="3Bot Name"
                            required
                            persistent-hint
                        ></v-text-field>
                        <v-checkbox
                            v-model="internetCapacity"
                            label="I want to learn more about how i can provide Internet capacity to people around me"
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
                            v-model="email"
                            :rules="emailRules"
                            label="E-mail"
                            required
                            validate-on-blur
                        ></v-text-field>

                        <v-checkbox
                            v-model="canSendEmail"
                            label="I agree to being kept informed about this new Internet by email. (Your data is safe with us, see our privacy policy here)"
                            :rules="[v => !!v || 'You must agree to continue!']"
                        />

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
                        ><v-icon
                            >fas fa-chevron-left</v-icon
                        ></v-btn
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
            email: '',
            emailRules: [
                v => !!v || 'E-mail is required',
                v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
            ],
            threeBotNameRules: [
                v => v.length <= 20 || 'Name must be less than 20 characters',
                v => /^[a-zA-Z0-9]+$/.test(v) || 'Please use alphanumerics charachters only (0-9 and a-z)',
            ],
            userNameRules: [
                v => v.length <= 40 || 'Name must be less than 40 characters',
                v => /^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$/.test(v) || 'Name must be valid',
            ],
            userName: '',
            threeBotName: '',
            reserve_3bot: false,
            ITSolutions: false,
            internetCapacity: false,
            canSendEmail: false,
            loading: false,
        }),
        methods: {
            async validateAndSubmit() {
                if (!this.$refs.form.validate()) {
                    return;
                }
                this.loading = true;

                const response = await axios.put(`/api/user`, {
                    email_address: this.email,
                    name: this.userName,
                    double_name: this.threeBotName,
                    internet_capacity: this.internetCapacity,
                    deploy_solutions: this.ITSolutions,
                });
                if (!response.data.success) {
                    await router.push('error');
                    return;
                }
                await router.push('thankyou');
            },
        },
    };
</script>
