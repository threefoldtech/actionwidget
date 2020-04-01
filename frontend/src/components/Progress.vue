<template>
    <div class="progress">
        <v-stepper class="ma-0" :elevation="0" :value="step">
            <v-stepper-header>
                <v-stepper-step step="1">Intro</v-stepper-step>

                <v-divider></v-divider>
                <v-stepper-step step="2">Declaration</v-stepper-step>

                <v-divider></v-divider>

                <v-stepper-step step="3">Threefold</v-stepper-step>
                <v-divider></v-divider>

                <v-stepper-step step="4">Sign up</v-stepper-step>
                <v-divider></v-divider>

                <v-stepper-step step="5">Referral</v-stepper-step>
            </v-stepper-header>
        </v-stepper>
    </div>
</template>

<script>
    export default {
        name: 'Progress',
        props: { step: { type: String, default: null, required: false } },
    };
</script>

<style scoped lang="scss">
    .v-stepper {
        box-shadow: none;
    }
</style>
