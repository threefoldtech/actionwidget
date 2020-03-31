module.exports = {
    transpileDependencies: ['vuetify'],
    devServer: {
        watchOptions: {
            poll: true,
        },
        proxy: {
            '/api': {
                logLevel: 'debug',
                target: 'http://localhost:5000',
            },
        },
    },
    configureWebpack: {
        optimization: {
            splitChunks: {
                chunks: 'initial',
                minSize: 1000,
                maxSize: 0,
                cacheGroups: {
                    vendors: {
                        test: /[\\/]node_modules[\\/]/,
                        name: 'vendors',
                        priority: 10,
                        enforce: true, // create chunk regardless of the size of the chunk
                        //maxSize: 10000
                    },
                },
            },
        },
        devtool: 'source-map',
    },
};
