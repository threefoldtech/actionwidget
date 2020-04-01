<template>
    <div class="intro__page">
        <v-container class="fill-height" fluid>
            <v-row align="center" justify="center">
                <v-card class="mt-5 py-6 mx-auto" max-width="800" tile>
                    <Progress step="3" />
                    <v-container fluid>
                        <v-row>
                            <v-col cols="12" sm="12">
                                <p>
                                    We use the Internet every day, yet most of
                                    us don’t know, or think, too much about it.
                                    How does the Internet work? Who runs / owns
                                    it? Is it good? Bad? Neutral?<br /><br />

                                    Despite serving our daily needs rather well
                                    until today, the Internet is now reaching a
                                    critical point. It now struggles with global
                                    data demands, and the overly-complex
                                    architecture behind it is rather
                                    centralized, making it inefficient and
                                    unsustainable.<br /><br />

                                    Did you know that about half of the world’s
                                    population remains unconnected to the
                                    Internet? High infrastructure and
                                    distribution costs make the Internet
                                    inaccessible to many.<br /><br />

                                    According to some statistics, the Internet
                                    industry today is worth in the trillions of
                                    dollars, 80% of which is owned by less than
                                    20 companies that profit out of users' data.
                                    Doesn’t seem fair, does it?<br /><br />

                                    We see a lot in the press about the airline
                                    industry’s negative impact on the
                                    environment, yet the Internet consumes
                                    between 5% and 10% of global energy. With
                                    growing demand from users and emerging
                                    technologies such as Internet of Things,
                                    artificial intelligence, or blockchain, this
                                    is expected to increase rapidly in the near
                                    future.<br /><br />

                                    A new Internet is needed, for both our
                                    planet and for humanity. One that is owned
                                    by the people. One that is equal to all and
                                    provides data ownership to its users. One
                                    that is environmentally-conscious. And one
                                    that can support all our innovations and
                                    experiences.<br /><br />

                                    This Internet does exist. Follow the next
                                    steps.
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
                </v-card>
            </v-row>
            <v-row align="center" justify="center"></v-row>
        </v-container>
    </div>
</template>
