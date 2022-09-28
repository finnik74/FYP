import Vue from 'vue'
import App from './App.vue'
import './plugins/element.js'
import './finnik.css'
Vue.config.productionTip = false
import VueRouter from "vue-router";
import router from './router'
Vue.use(VueRouter)
import BootstrapVue from 'bootstrap-vue'
Vue.use(BootstrapVue)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import animated from 'animate.css'

Vue.use(animated)

new Vue({
  el:'#app',
  router,
  render: h => h(App),
}).$mount('#app')









