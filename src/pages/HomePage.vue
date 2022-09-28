

<template>
 <div>
   <div class="jumbotron" style="height: 100vh">
     <div class="container" style="text-align: center;">
       <div style="margin-top: 35vh">
       <h1>欢迎来到Hao的主页</h1>
       <p>Keep calm and carry on.</p>
       <p @click="gomain"><a class="btn btn-primary btn-lg" role="button">关于我，了解更多</a></p>
       </div>
     </div>
   </div>
  <div style="height: 100vh" v-show="showmain">
  <div id="homepage" >
    <div class="animate__animated animate__pulse wow">
     <img class="imghao" src="../picture/finnik.jpeg" style="width: 200px;border-radius: 10px;margin-bottom: 30px;margin-top: 30px">
     <div class="title1">
      <span>储  昊 </span>
      <el-divider direction="vertical"></el-divider>
      <span> Hao Chu</span>
     </div>
     <div class="title2">
      <p><i class="el-icon-phone"></i> Phone: +86 13706153827</p>
      <p><i class="el-icon-s-promotion"></i> Mail: finnik74@outlook.com</p>
      <p><i class="el-icon-s-home"></i> Address: Liverpool</p>
     </div>
    </div>
    <div style="display: flex; justify-content: center" class="animate__animated animate__backInRight wow">
     <div class="wid" style="white-space: pre-wrap;font-family: 'BM Yeonsung';text-align: left" >
     <p style="font-size: 40px; text-align: center">About me</p>
     <p style="font-size: 20px; line-height: 20px;"  >{{content}}</p>
     </div>
    </div>
    <el-button type="info" plain @click="goKitchen">Finnik's kitchen</el-button>
  </div>

  <div style="height: 30px; display: flex; background-color: #475669; margin-top: 400px;width: 100%"> <div style="color: aliceblue; align-self: center;">&nbsp&nbsp&nbsp@ Developed by Hao Chu </div></div>
  <el-backtop style="margin-bottom: 50px">
      <div
          style="{
        height: 100%;
        width: 100%;
        background-color: #f2f5f6;
        box-shadow: 0 0 6px rgba(0,0,0, .12);
        text-align: center;
        line-height: 40px;
        color: gray;
      }"
      >
        UP
      </div>
  </el-backtop>
  </div>
 </div>
</template>






<script>
import { WOW } from 'wowjs'
export default {
  name: 'HomePage',
  props: {
    msg: String
  },
  data(){
    return{
      showmain:true,
      content:'I was born in Yixing, Jiangsu, the hometown of teapot. I finished 12 years of school life there.To be honest, my grades in primary and middle school were barely satisfactory, but in high school was terrible. It was the worst time of my life in some ways. Fortunately, it finally passed and I went to university.\n\n' +
          'I graduated from XJTLU in Suzhou,and my major was computer science, it was a 2+2 programme, which means I studied two years in Suzhou and two years in Liverpool. During my days in Liverpool, life became boring, but it also allowed me to have some free time to do things that I liked, such as software development and cooking, which is why I set up this website in the first place. ' +
          '\n\nHope you can find something you like  from my website!\n\n'
    }
  },
  methods:{
    goKitchen() {
      window.location.href='kitchen'
    },
    gomain(){
      var main = document.querySelector('#homepage')
      main.scrollIntoView({
            behavior: "smooth", // 默认 auto
            block: "start", // 默认 center
          })
    }
  },
  mounted() {
    document.title='Hao Chu'
    var wow = new WOW({
      boxClass: 'wow',    //需要执行动画元素的Class
      animateClass: 'animated',    //animation.css动画的Class
      offset: 0,    //距离可视区域多少开始执行动画
      mobile: false,   //是否在移动设备执行动画
      live: true    //异步加载的内容是否有效
  })
    wow.init();
  },
  created: function () {
  }
}
</script>

<style scoped>
html,body{
  height: 100%;
  margin: 0px;
  padding: 0px;
}
#homepage {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex; flex-direction: column; align-items: center;
}
.title1{
  font-size: 5rem;
  font-weight: initial;
}
.title2{
  font-size: 20px;
  line-height:10px;
  margin-bottom: 30px;
  margin-top: 30px;
}
</style>
