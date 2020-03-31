<template>
    <div class="status">
        <h1>status</h1>
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

            const refererToken = response.data.data.referer_token;

            this.referrals = await axios.get(
                `/api/referral_done/${refererToken}`
            );
        },
        data: function() {
            return { verifyToken: null, referrals: null };
        },
    };
</script>

<style scoped></style>
