<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  components: {
  },
  data() {
    return {
      routerAlive:true
    };
  },
  methods: {
  },
  computed:{

  },
  mounted() {
  }
}
</script>

<style>

#app{
  height: 100%;
}
</style>


