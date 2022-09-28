<template>
  <div  id="app">
   <p  class="title" style="color: #f2f5f6;margin-bottom: 50px; margin-top: 100px">Log in or Register Finnik's website</p>
    <div class="wid"  style="background-color: cornsilk; border-radius: 10px; margin-bottom: 60%; padding: 20px">
      <div>
        <el-radio-group class="center" v-model="radio">
          <el-radio-button label="Login"></el-radio-button>
          <el-radio-button label="Register"></el-radio-button>
        </el-radio-group>
      </div>


      <el-divider></el-divider>



      <el-form v-if="radio=='Login'" ref="form" :model="form"  size="big" style="padding:0px 10px 10px 10px; ">
        <el-form-item label="Username" hide-required-asterisk="false">
          <el-input placeholder="Enter your username." v-model="form.LoginUserName"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input  placeholder="Enter your password." v-model="form.password" type="password"></el-input>
        </el-form-item>
        <div class="center"><el-button  @click="LoginCheckRemote" type="primary">Login</el-button></div>
      </el-form>

      <el-form v-if="radio=='Register'" ref="form" :model="form"  size="big" style="padding:0px 10px 10px 10px;">
        <el-form-item label="Username">
          <el-input placeholder="Enter your username." v-model="form.RegisterUserName"></el-input>
        </el-form-item>
        <el-form-item label="Password">
          <el-input placeholder="Enter your password." v-model="form.RegisterPassword"  type="password"></el-input>
        </el-form-item>
        <el-form-item label="Confirm Password">
          <el-input placeholder="Reenter your password." v-model="form.cpassword"  type="password"></el-input>
        </el-form-item>
        <el-form-item label="Birthday">
          <el-date-picker type="date" placeholder="Choose birthday" value-format="yyyy-MM-dd"  v-model="form.date1" style="width: 100%;">placement="bottom-start"</el-date-picker>
        </el-form-item>
        <div class="center">
          <el-button @click="UserSubmit" type="primary" slot="reference">Register</el-button>
        </div>
      </el-form>
    </div>
  </div>


</template>

<script>

import {getUserInfo, postUserInfo, postData} from "@/api/api";
export default {
  data() {
    return {
      form: {
        LoginUserName:'',
        RegisterUserName:'',
        RegisterPassword:'',
        password:'',
        cpassword:'',
        date1:''
      },
      radio:'Login',

    }
  },
  methods: {

    LoginCheckRemote() {
      let data = {'user': this.form.LoginUserName, 'password': this.form.password};
      this.axios({
        url: 'http://localhost:8000/auth/',
        method:'post',
        data:{
          name: this.form.LoginUserName,
          password: this.form.password
        },
        responseType: 'json'
      }).then(res => {
        console.log(res.data)
        if (res.data.status == 'success') {
          this.$message({message: 'Login successfully!', center: true});
          window.location.href='kitchen'+'?user='+this.form.LoginUserName;
        } else {
          this.$message({message: res.data.message, center: true})
        }
      })
    },

    UserSubmit () {
      if(this.form.RegisterPassword==''||this.form.RegisterUserName==''||this.form.cpassword==''||this.form.date1=='')
      {
        this.$message({message: 'Please input all the information!', center: true});
      }
      else if (this.form.RegisterPassword!=this.form.cpassword){
        this.$message({message: 'Password and confirmation are not the same!', center: true});
      }
      else if(this.form.RegisterPassword.length<8){
        this.$message({message: 'Password should be at least 8 letters.', center: true});
      }
      else{
        this.axios({
          url: 'http://localhost:8000/register/',
          method:'post',
          data:{
            name: this.form.RegisterUserName,
          },
          responseType: 'json'
        }).then(res => {
          console.log(res.data)
          if (res.data.status == 'success') {
            postUserInfo(this.form.RegisterUserName, this.form.RegisterPassword,this.form.date1).then(response => {
              this.$message({
                message: 'Register successfully!',
                center: true
              });
            })
          } else {
            this.$message({message: res.data.message, center: true})
          }
        })
      }
    },
  },
  mounted() {
    document.title = 'Login'
  }
}
</script>

<style scoped>
@import "../../src/finnik.css";
#app{
  background-color: lightblue;
  background-image: url('../picture/南校.jpeg');
  background-size: cover;
   display: flex;
  flex-direction: column;
  align-items: center;
}

</style>
