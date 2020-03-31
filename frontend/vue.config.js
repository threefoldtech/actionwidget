module.exports = {
    transpileDependencies: ['vuetify'],
    devServer: {
        proxy: {
          '/api': {
            logLevel: 'debug',
            target: 'http://localhost:5000'
          }
        }
      }
};
