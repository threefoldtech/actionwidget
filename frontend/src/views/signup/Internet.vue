<template>
    <div class="signup_internet">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" width="800" tile>
                    <Progress step="1" />
                     <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <h2>
                                   I acknowledge that          
                                </h2>
                            </v-col>
                        </v-row>

                    </v-container>
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
                                    >It is not acceptable that 50% of the global population remains without Internet access today.</v-list-item-title
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
                                    >The Internet is using too much energy (10% of the world's electricity).</v-list-item-title
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
                                    >I have become a cyborg, in a way, as my devices such as my smartphone and laptop have become extensions of myself.</v-list-item-title
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
                                    >Those devices aren’t owned by me. I am part of some big AI-driven Internet cloud.</v-list-item-title
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
                                    >where I can trust my country to protect my
                                    safety and rights</v-list-item-title
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
                                    >which is available everywhere in the world
                                    at a cost lower than
                                    today</v-list-item-title
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
                                    >Supported by a token that has real value
                                    and represents this new internet <br />
                                    (not like dollars trillions will be printed,
                                    not like bitcoin no
                                    backing)</v-list-item-title
                                >
                            </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                    <v-btn
                        class="btn__next"
                        color="#1072ba"
                        elevation="3"
                        fab
                        mini
                        to="signup"
                        dark
                        ><v-icon class="ml-1">fas fa-chevron-right</v-icon></v-btn
                    >
                </v-card>
            </v-row>
            <v-row align="center" justify="center"></v-row>
        </v-container>
    </div>
</template>
