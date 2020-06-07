import Vue from 'vue'
import App from './App.vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import routes from './routes'

Vue.use(Vuex)
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

Vue.use(VueRouter)
const router = new VueRouter({
  routes // short for `routes: routes`
})


new Vue({
  render: h => h(App),
  router: router,
}).$mount('#app')
