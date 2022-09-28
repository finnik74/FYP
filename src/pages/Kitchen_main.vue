<template>
  <div>
    <div class="colcentre bar" style=" font-size: 1.4rem; line-height: 60px; position: absolute;">
      <span>&nbsp;</span>
      <span style=""><el-button plain size="mini" @click="showbar =! showbar"><span  class="glyphicon glyphicon-align-justify"></span></el-button></span>
      <span @click="go_home" class="h">&nbsp;&nbsp;&nbsp;HomePage</span>
      <span @click="go_login" class="h" style="position: absolute; right: 1%">&nbsp;Login</span>
      <transition name="el-zoom-in-top">
        <navigation  v-show="showbar" style="top: 60px;position: absolute;z-index:999"></navigation>
      </transition>
    </div>



    <div class="container">
      <div id="app_main" class="wid">
       <h1 class="title" style="margin-top: 100px">Finnik's Kitchen</h1>
       <div class="picwid">
         <el-carousel :interval="4000" v-show="show1">
          <el-carousel-item v-for="item in imagebox" :key="item.id"  >
            <img :src="item.idView" style="height: 100%; width: 100%">
          </el-carousel-item>
         </el-carousel>

         <el-carousel :interval="4000" v-show="show2" type="card">
          <el-carousel-item v-for="item in imagebox" :key="item.id"  >
            <img :src="item.idView" style="height: 100%; width: 100%">
          </el-carousel-item>
         </el-carousel>
       </div>

        <div class="wid" style="margin-bottom: 30px">
          <el-divider content-position="left">Cooking is wonderful and interesting.</el-divider>
        </div>

        <el-tabs type="border-card" style="">
          <el-tab-pane>
            <span slot="label"><i class="el-icon-food"></i> 快速菜</span>
            <div class="templateItem">


                <div class="thumbnail template">
                  <img src="../picture/food/steam——fish.jpg">
                  <div class="caption">
                    <h3>Thumbnail label</h3>
                    <p>...</p>
                    <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                  </div>
                </div>



                <div class="thumbnail template">
                  <img src="../picture/food/steam——fish.jpg">
                  <div class="caption">
                    <h3>Thumbnail label</h3>
                    <p>...</p>
                    <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                  </div>
                </div>



                <div class="thumbnail template">
                  <img src="../picture/food/steam——fish.jpg">
                  <div class="caption">
                    <h3>Thumbnail label</h3>
                    <p>...</p>
                    <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                  </div>
                </div>



                <div class="thumbnail template" style="margin-right:0">
                  <img src="../picture/food/steam——fish.jpg">
                  <div class="caption">
                    <h3>Thumbnail label</h3>
                    <p>...</p>
                    <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                  </div>
                </div>

              <div class="thumbnail template">
                <img src="../picture/food/steam——fish.jpg">
                <div class="caption">
                  <h3>Thumbnail label</h3>
                  <p>...</p>
                  <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                </div>
              </div>

              <div class="thumbnail template" style="margin-right: 0">
                <img src="../picture/food/steam——fish.jpg">
                <div class="caption">
                  <h3>Thumbnail label</h3>
                  <p>...</p>
                  <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                </div>
              </div>





            </div>
          </el-tab-pane>
          <el-tab-pane>
            <span slot="label"><i class="el-icon-dish"></i> 慢速菜</span>
            <div class="templateItem">
              <div class="thumbnail template">
                <img src="../picture/food/steam——fish.jpg">
                <div class="caption">
                  <h3>Thumbnail label</h3>
                  <p>...</p>
                  <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                </div>
              </div>

              <div class="thumbnail template">
                <img src="../picture/food/steam——fish.jpg">
                <div class="caption">
                  <h3>Thumbnail label</h3>
                  <p>...</p>
                  <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                </div>
              </div>

              <div class="thumbnail template">
                <img src="../picture/food/steam——fish.jpg">
                <div class="caption">
                  <h3>Thumbnail label</h3>
                  <p>...</p>
                  <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                </div>

              </div>
              <div class="thumbnail template">
                <img src="../picture/food/steam——fish.jpg">
                <div class="caption">
                  <h3>Thumbnail label</h3>
                  <p>...</p>
                  <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                </div>
              </div>

              <div class="thumbnail template" style="margin-right: 0px">
                <img src="../picture/food/steam——fish.jpg">
                <div class="caption">
                  <h3>Thumbnail label</h3>
                  <p>...</p>
                  <p><a href="#" class="btn btn-primary" role="button">Button</a> <a href="#" class="btn btn-default" role="button">Button</a></p>
                </div>
              </div>
            </div>
          </el-tab-pane>

        </el-tabs>







   </div>
  </div>

    <div style="height: 30px; display: flex; background-color: #475669; margin-top: 400px;width: 100%"> <div style="color: aliceblue; align-self: center;">&nbsp&nbsp&nbsp@ Developed by Hao Chu </div></div>
  </div>
</template>


<style>
body{
  margin: 0px;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}

.flex {
  display: flex;
  flex-flow: row wrap;
  margin-top: 10px;
}
.flex div {
  width: 60px;
  height: 60px;
  margin-bottom: 5px;
  border: 1px solid black;
}

.templateItem {
  display: flex;
  flex-flow: row wrap;
}


.template {
    flex: 2 0 21%;
    margin-right: 2.2%;

  }
</style>

<script>
import navigation from "@/components/navigation";
import rolling_picture from "@/components/rolling_picture";
export default {

  data() {
    return{
      showbar:false,
      show1:true,
      show2:false,
      wid: document.body.clientWidth,
      imagebox:[{id:0,idView:require('../picture/food/steak.jpg')},
        {id:1,idView:require('../picture/food/steam——fish.jpg')},
        {id:2,idView:require('../picture/food/lu_beef.jpg')}
      ],
    }
  },
  methods: {
    go_login() {
      window.location.href='login'
    },
    go_home() {
      window.location.href='/'
    },
    resize_c(){
      this.wid = document.body.clientWidth
      console.log(this.wid)
      if (this.wid>1000){
        this.show1 = false
        this.show2 = true
      }
      console.log(this.show1)
    }

  },
  components:{
    navigation,
    rolling_picture
  },
  watch:{
    wid (val) {
      this.wid = val
    }
  },
  mounted() {
    document.title='Kitchen'
    this.resize_c()

  },

}
</script>
