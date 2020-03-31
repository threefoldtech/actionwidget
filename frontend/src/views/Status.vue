<template>
    <div class="status">
        <h1>status</h1>
        invitelink: {{refererToken}}
        <v-btn :to="{name: 'signup_reffered', params:{'userid': userId}}">test</v-btn>
        <code>
            {{ referrals }}
        </code>
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
            return { verifyToken: null, referrals: null, refererToken: null, userId: null };
        },
    };
</script>

<style scoped></style>
