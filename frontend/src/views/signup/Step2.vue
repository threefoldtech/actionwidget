<template>
    <div class="signup__step2">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class=" mt-5 py-6 mx-auto" max-width="800" tile>
                    <v-form
                        class="ma-5"
                        lazy-validation
                        ref="form"
                        v-model="valid"
                    >
                        <v-checkbox label="I want to reserve my digital twin" />
                        <v-checkbox
                            label="I am interested to have my own video conferencing solution which allows me to communicate with everyone in the world"
                        />
                        <v-checkbox
                            label="I am interested in a peer2peer alternative social media network for private & business usage"
                        />
                        <v-checkbox
                            label="I am interested to learn more about become a farmer and provide internet capacity for people around me"
                        />
                        <v-checkbox
                            label="I am interested to know more about how to deploy my own IT solutions on this new internet (maybe not)"
                        />
                        <v-btn
                            :disabled="!valid"
                            @click="validateAndSubmit"
                            class="mr-4"
                            color="success"
                        >
                            Next
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

    export default {
        name: 'Step2',
        methods: {
            async validateAndSubmit() {
                if (!this.$refs.form.validate()) {
                    return;
                }

                await axios.put(`/api/set_referral_and_currency`, {});

                router.push('signup_step_2');
            },
        },
    };
</script>
