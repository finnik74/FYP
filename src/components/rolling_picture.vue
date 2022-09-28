
<template>
  <el-carousel :interval="4000">
    <el-carousel-item v-for="item in imagebox" :key="item.id"  >
      <img :src="item.idView" style="height: 100%; width: 100%">
    </el-carousel-item>
  </el-carousel>
</template>

<script>
export default{
  data(){
    return {
      imagebox:[{id:0,idView:require('../picture/food/steak.jpg')},
        {id:1,idView:require('../picture/food/steam——fish.jpg')},
        {id:2,idView:require('../picture/food/lu_beef.jpg')}
      ],
    }
  },
  methods:{

  },
  mounted() {


  }
}
</script>

<style>



.img{
  height: 100%;
  height: auto;
}
</style>
