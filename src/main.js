import Vue from 'vue'
import App from './App.vue'
import './finnik.css'
Vue.config.productionTip = false
import VueRouter from "vue-router";
import router from './router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import animated from 'animate.css'
import Element from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(Element)
Vue.use(VueRouter)
Vue.use(animated)

new Vue({
  el:'#app',
  router,
  render: h => h(App),
}).$mount('#app')









