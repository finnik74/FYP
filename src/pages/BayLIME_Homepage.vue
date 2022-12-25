<template>
  <div  style="background-color:#C1DFF7;">
    <div class="jumbotron"  style="background-color:#C1DFF7; color: #f2f5f6; min-height: 100vh; padding:0px">
      <TopBar></TopBar>
      <div class="container animate__animated animate__fadeInDown" style="text-align: center;">
        <div style="margin-top: 12vh; margin-bottom: 6%; color: #2c3e50;" >
             <p style="font-size: 10vh; font-family: 'Al Bayan';text-shadow:0 3px #666 ">Web-BayLIME</p>
        </div>
        <div>
          <div class="box">
          <el-tabs v-model="activeName"   @tab-click="handleClick">
            <el-tab-pane label="XAI" name="first">
              <h1>What is XAI ?</h1>
              In recent years, the application of AI in several fields have all met huge resistance for the doubt of the models. However, the model obtained by deep learning is a black box, which means no information about the model behaviour can be obtained from the structure or weight of the model.XAI can solve the problem of opaque technical details under the deep learning mechanism so that developers can obtain detailed information in the development process through XAI tools and help developers troubleshoot or improve the model's performance through the obtained understandable information.
            </el-tab-pane>
            <el-tab-pane label="LIME" name="second">
              <h1>What is LIME ?</h1>
              LIME (local interpretable model-agnostic explanations) has been one of the most popular XAI tools these years. Its main
              idea is to use an interpretability model to predict the local approximation of the black box model. This method is mainly
              according to the change in the point of interest to train an explanatory model and it also weights each feature rather than
              making slight input disturbance to detect changes [5].<p></p>
              The core math formula of LIME can be represented as follows:<p></p>
              <h3 style="text-align: center">explanation(x) = argming∈GL(f, g, πx) + Ω(g) [2]</h3><p></p>
              Generally, concerning an explanation of model g in instance x, it is common to minimize a loss function to compare the
              approximation of model g and the original model f. In the formula above, Ω(g) means the model complexity of the explanation
              model g, while G stands for all possible explanation models, πx defines the neighbourhood of x. By the minimum of L, We make
              the interpretation of model f possible [6]. In addition, the model g, the neighbourhood range size, and the model complexity
              need to be defined [2]. Briefly, the working principle of LIME can be described as follows: The interpretability model is first
              determined for structured data, the exciting point x, and the neighbourhood range. LIME first samples globally, then for all
              sampled points, select the neighbourhood of interest point x, and then uses the neighbourhood range of interest point to fit the
              interpretability model.<p></p>
              However, the drawback of lime is also apparent. When sampling, LIME applies a straightforward random uniform opera-
              tion [7]: LIME may make different explanations for the same prediction. The randomness of LIME to the repeat of the process
              may result in the randomness generated in the dataset. Thus it is unstable and may produce inconsistent [8].
            </el-tab-pane>
            <el-tab-pane label="BayLIME" name="third">
              <h1>What is BayLIME ?</h1>
              Dr Zhao proposed a new approach–BayLIME to solve this problem. Bayesian linear regressor is used as a local surrogate
              model in BayLIME. The three cases concerning it are: (i) no prior knowledge; (ii) knowledge about the prior distribution of
              the coefficients, but do not know noise in the data; (iii) a comprehensive knowledge of the priors and noise of the coefficients.
              With partial and complete information, BayLIME is significantly superior to LIME on consistency, while BayLIME with non-
              informative priors does not. Because non-informative priors BayLIME only adopt randomly created information from the new
              data. If the process are repeated, the degree of coefficient will be directly proportional to the randomness of the samples in the
              dataset.<p></p>
              In conclusion, BayLIME embeds Bayesian modification on LIME. In other words, it successfully combines practical knowl-
              edge with a principled mechanism, which has been an clear trend in AI [9]. Consistency of repeated interpretations of the exact
              prediction and robustness to kernel Settings have been proven to be boosted by applying this combination. Although BayLIME
              is easy to use and effective, it may be difficult for beginners to understand how it works and how to use it. This project will
              modify BayLIME to strive to make it more concise. Moreover, the website visual GUI will make BayLIME easier for users to
              learn and use.
            </el-tab-pane>
            <el-tab-pane label="Reference" name="fourth">
              <h1>Reference</h1>
              [1] G. Karpagam, A. Varma, S. M, and S. S. V, “Understanding, visualizing and explaining xai through case studies,” in 2022
              8th International Conference on Advanced Computing and Communication Systems (ICACCS), vol. 1, 2022, pp. 647–654.<p></p>
              [2] M. T. Ribeiro, S. Singh, and C. Guestrin, “Why should i trust you?: Explaining the predictions of any classifier,” 2016.
              [Online]. Available: https://arxiv.org/abs/1602.04938<p></p>
              [3] X. Zhao, W. Huang, X. Huang, V. Robu, and D. Flynn, “Baylime: Bayesian local interpretable model-agnostic explanations,”
              in Proceedings of the Thirty-Seventh Conference on Uncertainty in Artificial Intelligence, ser. Proceedings of Machine Learning
              Research, C. de Campos and M. H. Maathuis, Eds., vol. 161. PMLR, 27–30 Jul 2021, pp. 887–896.<p></p>
              [4] E. Tjoa and C. Guan, “A survey on explainable artificial intelligence (xai): Toward medical xai,” IEEE Transactions on
              Neural Networks and Learning Systems, vol. 32, no. 11, pp. 4793–4813, 2021.<p></p>
              [5] E. Amparore, A. Perotti, and P. Bajardi, “To trust or not to trust an explanation: using leaf to evaluate local linear xai
              methods,” PeerJ. Computer science, vol. 7, pp. 1–26, 2021.<p></p>
              [6] B. Cheng, R. Xue, H. Yang, L. Zhu, and W. Xiang, “Dpn-senet:a self-attention mechanism neural network for detection and
              diagnosis of covid-19 from chest x-ray images.” 2021.<p></p>
              [7] S. Shi, X. Zhang, and W. Fan, “A modified perturbed sampling method for local interpretable model-agnostic explanation,”
              2020.<p></p>
              [8] M. R. Zafar and N. M. Khan, “Dlime: A deterministic local interpretable model-agnostic explanations approach for computer-
              aided diagnosis systems.” 2019.<p></p>
              [9] W. Huang, X. Zhao, and X. Huang, “Embedding and extraction of knowledge in tree ensemble classifiers,” 2021-09-02.6
            </el-tab-pane>
          </el-tabs>
          </div>
          <p style="color: #3B76EF; margin-top: 50px">Now, you must have know something about XAI, LIME and BayLIME.</p>
          <p></p>
          <p @click="gomain" style="margin-bottom: 10%"><a class="btn btn-primary btn-lg" role="button">Let's try !</a></p>
        </div>
      </div>
    </div>
    <div style="min-height: 100vh; background-color: #96caea" v-show="showmain">
      <div id="homepage">
        <div class="animate__animated animate__pulse wow">
          <div class="box" style="width: 80vw;margin-top: 10vh; margin-bottom: 10vh; box-shadow: 0 0 10px #666" >
          <el-tabs v-model="activeName2"   @tab-click="handleClick">
           <el-tab-pane label="BayLIME" name="first">
             <div class="templateItem">
               <div class="thumbnail template" style="text-align: center;background-color: #4b93f5">
                 <img src="../../../../../demoproject/BayLime/data/5.jpg">
                 <h2 style="color: #003bbb;font-weight: 500">Original</h2>
                 <el-tooltip class="item" effect="dark" content="Choose pattern" placement="right-start">
                   <el-select v-model="value5" placeholder="Choose pattern.">
                     <el-option
                         v-for="item in options5"
                         :key="item.value5"
                         :label="item.label5"
                         :value="item.value5">
                     </el-option>
                   </el-select>
                 </el-tooltip>
                 <p></p>
                 <el-tooltip class="item" effect="dark" content="Choose picture" placement="right-start">
                 <el-select v-model="value" placeholder="Please choose picture.">
                   <el-option
                       v-for="item in options1"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
                   </el-option>
                 </el-select>
                 </el-tooltip>
                 <p></p>
                 <el-tooltip class="item" effect="dark" content="if True, only take superpixels that positively contribute to
                the prediction of the label." placement="right-start">
                 <el-select v-model="value2" placeholder="Positive only">
                   <el-option
                       v-for="item in options2"
                       :key="item.value2"
                       :label="item.label2"
                       :value="item.value2">
                   </el-option>
                 </el-select>
                 </el-tooltip>
                 <p></p>
                 <el-tooltip class="item" effect="dark" content="if True, make the non-explanation part of the return
                image gray" placement="right-start">
                 <el-select v-model="value4" placeholder="Hidden rest">
                   <el-option
                       v-for="item in options4"
                       :key="item.value4"
                       :label="item.label4"
                       :value="item.value4">
                   </el-option>
                 </el-select>
                 </el-tooltip>
                 <p></p>
                 <el-tooltip class="item" effect="dark" content="number of superpixels to include in explanation" placement="right-start">
                 <el-select v-model="value3" placeholder="Number of features">
                   <el-option
                       v-for="item in options3"
                       :key="item.value3"
                       :label="item.label3"
                       :value="item.value3">
                   </el-option>
                 </el-select>
                 </el-tooltip>
                 <p></p>
                 <el-button @click="get_no_bay">Start</el-button>

                 <p></p>
               </div>

               <div class="thumbnail template" style="margin-right: 0px">
                 <div class="temp">
                  <div class="box2" v-loading="load_nobay">
                    <img :src="'data:image/png;base64,' + no_bay" style="width: 100%;object-fit: cover" v-show="no_bay!=''"/>
                     <p style="font-size: 1em;color: black">No Bay</p>
                   </div>

                   <div class="box2" v-loading="load_bnip">
                     <img :src="'data:image/png;base64,' + bnip" style="width: 100%;object-fit: cover" v-show="bnip!=''"/>
                     <p style="font-size: 1em;color: black">Bay non info prior</p>
                   </div>
                   <div class="box2" v-loading="load_bip">
                     <img :src="'data:image/png;base64,' + bip" style="width: 100%;object-fit: cover" v-show="bip!=''"/>
                     <p style="font-size: 1em;color: black">Bay info prior</p>
                   </div>
                   <div class="box2" v-loading="load_bipfa">
                     <img :src="'data:image/png;base64,' + bipfa" style="width: 100%;object-fit: cover" v-show="bipfa!=''"/>
                     <p style="font-size: 1em;color: black;">BayesianRidge inf prior fit alpha</p>
                   </div>
                 </div>
               </div>

             </div>
           </el-tab-pane>
            <el-tab-pane label="BayLIME-Profession" name="second">
<!--&lt;!&ndash;             Coming soon.&ndash;&gt;-->
              <el-upload
                  class="upload-demo"
                  drag
                  action="http://localhost:8000/upload/"
                  :before-remove="beforeRemove"
                  multiple
                  :limit="1"
                  :on-exceed="handleExceed"
                  :on-change="handleChange"
                  accept=".png, .jpg, .jepg">
<!--                <el-button  type="success" @click="upload">点击上传</el-button>-->
                <i class="el-icon-upload"></i>
                <div class="el-upload__text">Drop file here or <em>click to upload</em></div>
                <div class="el-upload__tip" slot="tip">jpg/png files with a size less than 500kb</div>
              </el-upload>

<!--              <el-form>-->

<!--                <el-form-item label="姓名" prop="name">-->
<!--                  <el-input v-model="name"></el-input>-->
<!--                </el-form-item>-->
<!--                <el-form-item>-->
<!--                  <el-upload ref="upfile"-->
<!--                             style="display: inline"-->
<!--                             :auto-upload="false"-->
<!--                             :on-change="handleChange"-->
<!--                             :file-list="fileList"-->
<!--                             action="#">-->
<!--                    <el-button  type="success">选择文件</el-button>-->
<!--                  </el-upload>-->
<!--                </el-form-item>-->
<!--                <el-form-item>-->
<!--                  <el-button  type="success" @click="upload">点击上传</el-button>-->
<!--                </el-form-item>-->
<!--              </el-form>-->

            </el-tab-pane>
          </el-tabs>
          </div>

        </div>

      </div>
      <el-backtop style="margin-bottom: 50px"><div style="{
        height: 100%;
        width: 100%;
        background-color: #f2f5f6;
        box-shadow: 0 0 6px rgba(0,0,0, .12);
        text-align: center;
        line-height: 40px;
        color: gray;
      }">UP</div></el-backtop>

    </div>
    <div style="height: 30px; display: flex; background-color: #475669; width: 100%"> <div style="color: aliceblue; align-self: center;">&nbsp&nbsp&nbsp@ Developed by Hao Chu </div></div>
  </div>
</template>

<script>
import { WOW } from 'wowjs'
import TopBar from "@/components/TopBar";
export default {
  name: "BayLIME_Homepage",
  components: {TopBar},
  props: {
    msg: String
  },
  data(){
    return{
      name:'',
      fileList:[],
      no_bay:'',
      activeName2: 'first',
      activeName: 'first',
      showbar:false,
      showmain:true,
      options5: [{value5: 'non_Bay', label5: 'non_Bay'}, {value5: 'Bay_non_info_prior', label5: 'Bay_non_info_prior'}, {value5: 'Bay_info_prior', label5: 'Bay_info_prior'}, {value5: 'BayesianRidge_inf_prior_fit_alpha', label5: 'BayesianRidge_inf_prior_fit_alpha'},],
      options2: [{value2: 'True', label2: 'True'}, {value2: 'False', label2: 'False'},],
      options4: [{value4: 'True', label4: 'True'}, {value4: 'False', label4: 'False'},],
      options3: [{value3: 'small', label3: 'small'},{value3: 'normal', label3: 'normal'},{value3: 'big', label3: 'big'}],
      options1: [{value: 'dog', label: 'dog'}, {value: 'cat', label: 'cat'}, {value: 'horse', label: 'horse'},],
      value: '', value2: '', value3: '', value4:'', value5:'',
      load_nobay:false, bnip:'',
      load_bnip:false, bip:'', load_bip:false,
      bipfa:'', load_bipfa:false,
      dialogImageUrl: '',
      dialogVisible: false,
      disabled: false
    }

    },
  methods:{
    handleClick(tab, event) {
      console.log(tab, event)
    },
    goKitchen() {
      window.location.href='kitchen'
    },
    gomain(){
      var main = document.querySelector('#homepage')
      main.scrollIntoView({
        behavior: "smooth", // 默认 auto
        block: "start", // 默认 center
      })
    },
    get_no_bay(){
      if(this.value==''||this.value2==''||this.value3==''||this.value4==''||this.value5==''){
        this.$message({message: 'Please ensure chose all the options.', center: true});
      }
      else {
        switch (this.value5){
          case 'non_Bay': this.load_nobay = true; break;
          case 'Bay_non_info_prior': this.load_bnip = true; break;
          case 'Bay_info_prior': this.load_bip = true;break;
          case  'BayesianRidge_inf_prior_fit_alpha':this.load_bipfa=true
        }
        this.$message({message: 'This may take a long time, please do not refresh and wait patiently.', center: true});
        this.axios({
          url: 'http://localhost:8000/bay/',
          method:'post',
          data:{
            'picture':this.value,'po':this.value2,'num':this.value3,'hr':this.value4,'pattern':this.value5
          },
          responseType: 'json'
        }).then(res => {
          console.log(res.data)
          var pattern = res.data['pattern']
          switch (pattern){
            case 'non_Bay':
              this.load_nobay = false
              this.no_bay = res.data['fig']
              break
            case 'Bay_non_info_prior':
              this.load_bnip = false
              this.bnip = res.data['fig']
              break
            case 'Bay_info_prior':
              this.load_bip = false
              this.bip = res.data['fig']
              break
            case 'BayesianRidge_inf_prior_fit_alpha':
              this.load_bipfa = false
              this.bipfa = res.data['fig']
          }
        })
      }

    },
    handleChange(file, fileList) {
      this.fileList = fileList;
      console.log(fileList)
    },
    // handleRemove(file, fileList) {
    //   console.log(file, fileList);
    // },
    // handlePreview(file) {
    //   console.log(file);
    // },
    handleExceed(files, fileList) {
      this.$message.warning(`The limit is 1, you selected ${files.length} files this time`);
    },
    beforeRemove(file, fileList) {
      return this.$confirm(`Remove ${ file.name }？`);
    },
    upload(){
      let fd = new FormData();
      fd.append("name",this.name);
      this.fileList.forEach(item=>{
        //文件信息中raw才是真的文件
        fd.append("file",item.raw);
        //console.log(item.raw)
      })
      console.log(fd)
      this.axios({
        url: 'http://localhost:8000/upload/',
        method:'post',
        data: {file: this.fileList[0].raw}
      }).then(res=>{
        console.log(res.data)
      })
    },


  },
  mounted() {
    document.title='BayLIME'
    var wow = new WOW({
      boxClass: 'wow',    //需要执行动画元素的Class
      animateClass: 'animated',    //animation.css动画的Class
      offset: 0,    //距离可视区域多少开始执行动画
      mobile: false,   //是否在移动设备执行动画
      live: false   //异步加载的内容是否有效
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
  display: flex; flex-direction: column; align-items: center;
}
.temp {
  /* basic */
  margin: 0 auto;
  padding: 0;
  height: 100%;
  width: 100%;
  /* flex布局 */
  display: flex;
  /* 主轴居中(由于) */
  /* justify-content: center; */
  /* 设定主轴为横轴 默认row，还可以column |row-reverse|column-reverse */
  flex-direction: row;
  /* 主轴上的对齐方式 */
  justify-content: space-between;
  /* 换行(类似浮动布局) */
  flex-wrap: wrap;
  /* 副轴居中 */
  /* align-items: center; */
  align-content: space-between;
}
.box2 {
  border: 2px solid black;
  border-radius: 5px;
  box-sizing: border-box;
  width: calc(50% - 2.5px);
  height: calc(50% - 2.5px);
  text-align: center;
  background-color: #d4f0fd;
  display: inline-block;
  font-size:20px;
  color: #303030;
  line-height: 1.6;
  word-wrap: break-word;
  word-break: break-word;
  overflow: hidden;
}

</style>
