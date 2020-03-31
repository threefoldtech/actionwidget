<template>
    <div class="signup">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class=" mt-5 py-6 mx-auto" max-width="800" tile>
                    <v-form ref="form" v-model="valid" lazy-validation class="ma-5">
                        <v-checkbox
                            :rules="[v => !!v || 'You must agree to continue!']"
                            label="I want to reserve my digital twin"
                            required
                        ></v-checkbox>
                        <v-checkbox
                            :rules="[v => !!v || 'You must agree to continue!']"
                            label="I am interested to have my own video conferencing solution which allows me to communicate with everyone in the world"
                            required
                        ></v-checkbox>
                        <v-checkbox
                            :rules="[v => !!v || 'You must agree to continue!']"
                            label="I am interested in a peer2peer alternative social media network for private & business usage"
                            required
                        ></v-checkbox>
                        <v-checkbox
                            :rules="[v => !!v || 'You must agree to continue!']"
                            label="I am interested to learn more about become a farmer and provide internet capacity for people around me"
                            required
                        ></v-checkbox>
                        <v-checkbox
                            :rules="[v => !!v || 'You must agree to continue!']"
                            label="I am interested to know more about how to deploy my own IT solutions on this new internet (maybe not)"
                            required
                        ></v-checkbox>
                        <v-btn
                            :disabled="!valid"
                            elevation="3"
                            fab mini
                            color="#1072ba"
                            dark
                            class="btn__next"
                            @click="validate"
                        >
                            Next
                        </v-btn>
                    </v-form>
                </v-card></v-row
            ></v-container
        >
    </div>
</template>
<script>
    import router from '../router';

    export default {
        data: () => ({
            valid: true,
        }),
        methods: {
            validate() {
                if (!this.$refs.form.validate()) {
                    return;
                }
                router.push('signup_cyborg');
            },
        },
    };
</script>
