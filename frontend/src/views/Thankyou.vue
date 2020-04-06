<template>

    <div class="thankyou__page">
    <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
            <v-card
                class="mt-5 py-6 mx-auto"
                width="800"
                tile
            >
                <p class="ma-4 text-center">Thank you to refer your friends!</p>
                



                        <v-row >
                            <v-col cols="12" sm="12">
                                    <h3>Visit us</h3>
                            </v-col>
                            <v-col cols="12" sm="6">
                                    <a :href="'https://threefold.io'" target="_blank">
                                        <v-col cols="12" sm="6">
                                                <v-img src="../assets/logo.png" height="45" width="150"></v-img> 
                                        </v-col>
                                    </a> 
                            </v-col>
                            <v-col cols="12" sm="6" class="mt-4">
                                    <a :href="'https://forum.threefold.io/'" target="_blank"><h4>Threefold forums</h4></a>
                            </v-col>                            
                        </v-row>



            </v-card>
        </v-row>
        <v-row align="center" justify="center">
            
        </v-row>
    </v-container>
    </div>
</template>

<script>
    export default {
        name: 'thankyou',
    };
</script>

<style scoped></style>
