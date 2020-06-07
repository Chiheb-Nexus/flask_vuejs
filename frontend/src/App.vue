<style lang="scss">
  @import "../node_modules/ag-grid-community/dist/styles/ag-grid.css";
  @import "../node_modules/ag-grid-community/dist/styles/ag-theme-alpine.css";
</style>

<template>
  <div id="app">
    <Navigation/>
    <!--<img alt="Vue logo" :src="logo">-->
    <router-view/>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Navigation from './components/Navigation.vue'
import Home from './components/Home.vue'
import logo from "./assets/logo.png"


export default {
  name: 'App',
  data: function(){
    return {
      logo: logo
    }
  },
  components: {
    'Navigation': Navigation,
    'Home': Home
  }
}
</script>
