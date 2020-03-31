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

            const refererToken = response.data.data.referer_token;

            this.referrals = await axios.get(
                `/api/referral_done/${refererToken}`
            );
        },
        data: function() {
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
        },
    };
</script>

<style scoped></style>
