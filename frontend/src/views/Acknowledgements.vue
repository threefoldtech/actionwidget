<template>
    <div class="intro__page">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <Progress step="2" />
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <h3>I acknowledge that I</h3>
                            </v-col>
                            <v-col cols="12" sm="12">
                                <ul class="ml-4">
                                    <li class="mb-2">
                                        Became a cyborg because I cannot live
                                        anymore without my smartphone.
                                    </li>

                                    <li class="mb-2">
                                        Realize that my cyborg part is not owned
                                        by me – I am part of some big AI-driven
                                        Internet cloud.
                                    </li>

                                    <li class="mb-2">
                                        Want my digital life back in such a way
                                        it's friendly to our planet and my human
                                        rights.
                                    </li>
                                    <li class="mb-2">
                                        Do not agree that the Internet is using
                                        up to 10% of the world's electricity –
                                        there must be a better alternative that
                                        is good for the planet.
                                    </li>
                                    <li class="mb-2">
                                        Agree we need to stop the global neutral
                                        Internet from disappearing – it's being
                                        cut into pieces, firewalls are installed
                                        everywhere, my data is abused,
                                        information is often fake or
                                        manipulated.
                                    </li>
                                </ul>

                                <p class="mt-4">
                                    I want to reserve my digital twin, a citizen
                                    of the new unbreakable Internet owned by all
                                    of us.
                                </p>
                            </v-col>
                        </v-row>
                    </v-container>

                    <v-btn
                        class="btn__next"
                        elevation="3"
                        fab
                        mini
                        to="signup"
                        color="#1072ba"
                        dark
                        ><v-icon class="ml-1"
                            >fas fa-chevron-right</v-icon
                        ></v-btn
                    >
                    <v-btn
                        class="btn__previous"
                        elevation="1"
                        fab
                        mini
                        to="intro"
                        color="#1072ba"
                        dark
                        ><v-icon>fas fa-chevron-left</v-icon></v-btn
                    >
                </v-card>
            </v-row>
            <v-row align="center" justify="center"></v-row>
        </v-container>
    </div>
</template>
