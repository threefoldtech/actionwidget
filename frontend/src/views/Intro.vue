<template>
    <div class="intro__page">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center" class="pa-2">
                <v-card class="mt-5 py-6 mx-auto" width="800" tile>
                    <Progress step="1" />

                    <v-row align="center" justify="center" class="ma-4">
                        <v-img
                            src="../assets/Desktop_Landing.png"
                            aspect-ratio="1"
                            class="grey lighten-2 hidden-sm-and-down"
                            max-width="800"
                            max-height="600"
                        ></v-img>
                        <v-img
                            src="../assets/Mobile_Landing.png"
                            aspect-ratio="1"
                            class="grey lighten-2 hidden-lg-and-up"
                            max-width="600"
                            max-height="600"
                        >
                            <template v-slot:placeholder>
                                <v-row
                                    class="fill-height ma-0"
                                    align="center"
                                    justify="center"
                                >
                                    <v-progress-circular
                                        indeterminate
                                        color="grey lighten-5"
                                    ></v-progress-circular>
                                </v-row>
                            </template>
                        </v-img>
                    </v-row>
                    <v-btn
                        elevation="2"
                        fab
                        mini
                        color="#1072ba"
                        class="btn__next white--text"
                        to="acknowledgements"
                    >
                        <v-icon class="ml-1">fas fa-chevron-right</v-icon>
                    </v-btn>
                </v-card>
            </v-row>
            <v-row align="center" justify="center"></v-row>
        </v-container>
    </div>
</template>
