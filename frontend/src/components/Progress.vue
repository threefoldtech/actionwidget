<template>
    <div class="progress">
        <v-stepper class="ma-0" :elevation="0" :value="step">
            <v-stepper-header>
                <v-stepper-step step="1">intro</v-stepper-step>

                <v-divider></v-divider>
                <v-stepper-step step="2">declaration</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step step="3">threefold</v-stepper-step>
                <v-divider></v-divider>

                <v-stepper-step step="4">sign up</v-stepper-step>
                <v-divider></v-divider>

                <v-stepper-step step="5">referral</v-stepper-step>
            </v-stepper-header>
        </v-stepper>
    </div>
</template>

<script>
    export default {
        name: 'progress',
        props: { step: { type: Number } },
    };
</script>

<style scoped lang="scss">
    .v-stepper {
        box-shadow: none;
    }
</style>
