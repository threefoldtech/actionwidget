<template>
    <div class="intro__page">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <Progress step="2" />
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <h3>I acknowledge that</h3>
                            </v-col>
                            <v-col cols="12" sm="12">
                               <ul class="ml-4">
                                   <li>It is not acceptable that 50% of the global population remains without Internet access today</li>

                                   <li>The Internet is using too much energy (10% of the world's electricity)</li>

                                   <li>The global neutral Internet is disappearing (cut into pieces, firewalls installed everywhere, my data being abused, fake or manipulated information)</li>
                                   <li>I have become a cyborg, in a way, as my devices such as my smartphone and laptop have become extensions of myself</li>
                                   <li>Those devices aren’t owned by me. I am part of some big AI-driven Internet cloud</li>
                               </ul>
                            </v-col>
                        </v-row>
                         <v-row>
                            <v-col cols="12" sm="12">
                                <h3>Therefore, I declare that the Internet should</h3>
                            </v-col>
                            <v-col cols="12" sm="12">
                               <ul class="ml-4">
                                   <li>Be available everywhere in the world at a cost lower than today</li>

                                   <li>Provide everyone with equal chances to learn, partake and succeed</li>

                                   <li>Be sustainable for the planet and life</li>
                                   <li>Respect basic human rights</li>
                                   <li>Give me full ownership of my data and help me protect it</li>
                                   <li>Not abuse my personal information – we should not tolerate the way things are today</li>
                                   <li>Be available to my country to protect my individual rights and safety</li>
                                   <li>GBe supported by a token that enables me to use on demand</li>
                               </ul>
                            </v-col>
                        </v-row>
                    </v-container>

                    <v-btn
                        class="btn__next"
                        elevation="3"
                        fab
                        mini
                        to="threefold"
                        color="#1072ba"
                        dark
                        ><v-icon class="ml-1"
                            >fas fa-chevron-right</v-icon
                        ></v-btn
                    >
                </v-card>
            </v-row>
            <v-row align="center" justify="center"></v-row>
        </v-container>
    </div>
</template>
