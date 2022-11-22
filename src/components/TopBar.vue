<template>
  <div class="colcentre bay_bar" style=" font-size: 1.7rem; line-height: 50px; position: absolute;">
    <span>&nbsp;&nbsp;</span>
    <span style=""><el-button plain size="mini" @click="showbar =! showbar"><span  class="glyphicon glyphicon-align-justify"></span></el-button></span>
    <span @click="go_home" class="h">&nbsp;&nbsp;&nbsp;HomePage</span>
    <span @click="go_login" class="h" style="position: absolute; right: 1%">&nbsp;Login</span>
    <transition name="el-zoom-in-top">
      <navigation v-show="showbar" style="top: 60px;position: absolute;z-index:999"></navigation>
    </transition>
  </div>
</template>
<script>
import Navigation from "@/components/navigation";
export default {
  name: "TopBar",
  components: {Navigation},
  data() {
    return{
      showbar:false,
    }
  },
  methods: {
    go_login() {
      window.location.href='login'
    },
    go_home() {
      window.location.href='/'
    },

  },
}
</script>

<style scoped>

</style>
