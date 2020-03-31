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

            await axios.get(`/api/verify_user/${this.verifyToken}`);

            this.referrals = await axios.get(
                `/api/referral_done/${this.verifyToken}`
            );
        },
        data: function () {
            return { verifyToken: null, referrals: null };
        },
    };
</script>

<style scoped></style>
