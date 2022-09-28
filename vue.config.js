const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave:false,
  // devServer: {
  //   port: 8080,
  //   host: 'localhost',
  //   open: true,
  //   https: false,
  //   proxy: {
  //     'api': {
  //       target: 'https://localhost:',
  //       changeOrigin: true,
  //       ws: false,
  //       pathRewrite: {
  //         '^/apis': ''
  //       }
  //     }
  //   }
  // }
})
