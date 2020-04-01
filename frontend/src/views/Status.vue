<template>
    <div class="status">
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
                            <v-col cols="11" sm="11">
                                <v-text-field
                                    :label="referralUrl"
                                    disabled
                                    single-line
                                    >{{ referralUrl }}</v-text-field
                                >
                            </v-col>
                            <v-col cols="1" sm="1" class="pt-6">
                                <v-btn
                                    icon
                                    v-if="referralUrl"
                                    v-clipboard="referralUrl"
                                >
                                    <v-icon>fas fa-copy</v-icon>
                                </v-btn>
                            </v-col>
                        </v-row>
                        <v-row v-if="referrals.length">
                            <v-col cols="12" sm="12">
                                <h2>referred users ({{ referrals.length }})</h2>
                            </v-col>
                            <v-col cols="12" sm="12">
                                <v-data-table
                                    :headers="headers"
                                    :items="referrals"
                                    :items-per-page="10"
                                    elevation="0"
                                ></v-data-table>
                            </v-col>
                        </v-row>
                        <v-row v-else>
                            <v-col cols="12" sm="12">
                                <h2>No referred users</h2>
                            </v-col>
                        </v-row>
                    </v-container>
                </v-card>
            </v-row>
        </v-container>
    </div>
</template>

<script>
    import router from '../router';
    import axios from 'axios';
    import Vue from 'vue';
    import Clipboard from 'v-clipboard';
    Vue.use(Clipboard);

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

            this.referrerToken = response.data.data.referrer_token;
            this.userId = response.data.data.id;
            const host = window.location.host;
            const protocol = window.location.protocol;
            const baseUrl = `${protocol}//${host}`;
            this.referralUrl = `${baseUrl}/signup_referred?userid=${this.userId}`;
            const referralResponse = await axios.get(
                `/api/referral_done/${this.referrerToken}`
            );
            this.referrals = JSON.parse(referralResponse.data.data);
        },
        data: function() {
            return {
                verifyToken: '',
                referrals: [],
                referralUrl: null,
                referrerToken: null,
                userId: null,
                headers: [
                    {
                        text: '3Bot Name',
                        align: 'start',
                        value: 'referral_3bot_name',
                    },
                ],
            };
        },
    };
</script>
