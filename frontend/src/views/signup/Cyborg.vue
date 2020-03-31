<template>
    <div class="signup_cyborg">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class=" mt-5 py-6 mx-auto" max-width="800" tile>
                    <v-list-item-group color="primary">
                        <v-list-item>
                            <v-list-item-icon>
                                <v-simple-checkbox
                                    :value="true"
                                    disabled
                                ></v-simple-checkbox>
                            </v-list-item-icon>
                            <v-list-item-content>
                                <v-list-item-title
                                    >I acknowledge that I became a cyborg
                                    because I cannot live anymore without my
                                    smartphone.</v-list-item-title
                                >
                            </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-icon>
                                <v-simple-checkbox
                                    :value="true"
                                    disabled
                                ></v-simple-checkbox>
                            </v-list-item-icon>
                            <v-list-item-content>
                                <v-list-item-title
                                    >I realize that my cyborg part is not owned
                                    by me, I am part of some big AI driven
                                    internet cloud.</v-list-item-title
                                >
                            </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-icon>
                                <v-simple-checkbox
                                    :value="true"
                                    disabled
                                ></v-simple-checkbox>
                            </v-list-item-icon>
                            <v-list-item-content>
                                <v-list-item-title
                                    >I want my digital life back in such a way
                                    it&#39;s friendly to our planet and my human
                                    rights.</v-list-item-title
                                >
                            </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-icon>
                                <v-simple-checkbox
                                    :value="true"
                                    disabled
                                ></v-simple-checkbox>
                            </v-list-item-icon>
                            <v-list-item-content>
                                <v-list-item-title
                                    >I do not agree that the internet is using
                                    up to 10% of the world&#39;s electricity and
                                    this will become multiple times worse. There
                                    needs to be an alternative which is good for
                                    the planet.</v-list-item-title
                                >
                            </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                            <v-list-item-icon>
                                <v-simple-checkbox
                                    :value="true"
                                    disabled
                                ></v-simple-checkbox>
                            </v-list-item-icon>
                            <v-list-item-content>
                                <v-list-item-title
                                    >I do not agree that the global neutral
                                    internet is disappearing, it&#39;s being cut
                                    in pieces, firewalls are installed
                                    everywhere, my data is abused, information
                                    is often fake manipulated and there is not
                                    much we can do about it,
                                    ...</v-list-item-title
                                >
                            </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                    <v-row align="center" justify="center">
                        <p>
                            All of this is possible. ThreeFold has created a new
                            internet solution which allows: ...
                        </p>
                    </v-row>
                    <v-btn
                        class="btn__next"
                        elevation="3"
                        fab
                        mini
                        to="signup"
                        color="#1072ba"
                        dark
                        >next</v-btn
                    >
                </v-card>
            </v-row>
            <v-row align="center" justify="center"></v-row>
        </v-container>
    </div>
</template>

