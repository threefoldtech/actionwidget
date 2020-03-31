<template>
    <div class="status">
<<<<<<< HEAD
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" width="800" tile>
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <p>
                                    Copy following url to invite friends to the
                                    3bot app
                                </p>
                            </v-col>
                            <v-col cols="12" sm="6">
                                <v-text-field
                                    label="linkske"
                                    single-line
                                    append-icon="fas fa-copy"
                                ></v-text-field>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <h2>referred users ({{referrals.length}})</h2> 
                            </v-col>
                            <v-col cols="12" sm="12">
                                <v-data-table
                                    :headers="headers"
                                    :items="referrals"
                                    :items-per-page="10"
                                    class="elevation-1"
                                ></v-data-table>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card>
            </v-row>
        </v-container>
=======
        <h1>status</h1>
        invitelink: {{refererToken}}
        <v-btn :to="{name: 'signup_reffered', params:{'userid': userId}}">test</v-btn>
        <code>
            {{ referrals }}
        </code>
>>>>>>> 1d891d4a6e9f9a8fda27e92a0f1731b000b51a70
    </div>
</template>

<script>
    import router from '../router';
    import axios from 'axios';

    export default {
        name: 'status',
        async mounted() {
            if (!this.$route.query.verify_token) {
                router.push('error');
                return;
            }
            this.verifyToken = this.$route.query.verify_token;

            const response = await axios.post(
                `/api/verify_user/${this.verifyToken}`
            );

            this.refererToken = response.data.data.referrer_token;
            this.userId = response.data.data.user_id;

            this.referrals = (
                await axios.get(`/api/referral_done/${this.refererToken}`)
            ).data.data;
        },
        data: function() {
<<<<<<< HEAD
            return {
                verifyToken: 'sdfsdfsdf',
                referrals: null,
                headers: [
                    {
                        text: '3Bot Name',
                        align: 'start',
                        value: '3BotName',
                    },
                ],
            };
=======
            return { verifyToken: null, referrals: null, refererToken: null, userId: null };
>>>>>>> 1d891d4a6e9f9a8fda27e92a0f1731b000b51a70
        },
    };
</script>

<style scoped></style>
