module.exports = {
  publicPath: '/',
  devServer: {
    proxy: {
      '/api': {
        target: `${process.env.VUE_APP_API_URL}`,
      }
    }
  }
}