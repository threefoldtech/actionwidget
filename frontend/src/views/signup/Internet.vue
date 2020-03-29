<template>
    <div class="signup_internet">
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
                                    >which allows me to ownf my own data and
                                    digital life</v-list-item-title
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
                                    >where abuse of my information is not
                                    tolerated</v-list-item-title
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
                                    >without the need to burn crazy amounts of
                                    fossil fuel to provide my digital
                                    life</v-list-item-title
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
                                    >where everyone has equal
                                    chances</v-list-item-title
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
                    <v-btn class="btn__next" elevation="3" fab mini to="signup" color="primary">next</v-btn>
                </v-card>
            </v-row>
            <v-row align="center" justify="center"></v-row>
        </v-container>
    </div>
</template>
<style lang="scss" scoped>
    .btn__next{
        position: absolute;
        right: 10px;
        bottom: -28px;
    }
</style>
