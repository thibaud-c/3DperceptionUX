/**
MIT License

Copyright (c) [2020] [Thibaud Chassin]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/
<template lang="pug">
  #Main
    .level
      //stepper + language button 
      stepper(:steps.sync="step")
      button.button.is-text(@click='$i18n.locale = "en"')  EN
      button.button.is-text(@click='$i18n.locale = "fr"')  FR 
    .stage-size
      //pages
      welcome(v-if="step==0" @nextstage="add_step")
      socio(v-if="step==1" :user_name="user_name" @nextstage="add_step" @send_data_to_db="save_data")
      perception(v-if="step==2" :user_name="user_name" :scene_order="scene_order" :answer_order="answer_order" :scene_angles="scene_angles" @send_data_to_db="save_data" @nextstage="add_step")
      feedback(v-if="step==3" :user_name="user_name" :results="given_answer" @nextstage="add_step" @send_data_to_db="save_data")
</template>
  
<script>
import axios from 'axios';
import browserInfo from '../js/detect-browser.js'
//cfg
import GConfig from '../assets/config.json'
// pages imports
import stepper from './global/glob-stepper.vue'
import welcome from './instructions/intro-main.vue'
import socio from './sociographie/socio-main.vue'
import perception from './perception/perc-main.vue'
import feedback from './feedback/feed-main.vue'

export default {
  name: 'startsurvey',
  components : { 
    // liste des composants utilisés dans la div principale
    stepper,
    welcome,
    socio,
    perception,
    feedback
  },
  data () {
    return {
      version:1,
      id_poste:"",
      starting_date:"",
      user_name:"",
      user_config:{},
      user_ip_data:{},
      user_browser_data_auto:{},
      user_browser_data_manu:{},
      scene_order:[0,1,2,3],
      answer_order:[0,1,2,3],
      given_answer:[],
      scene_angles:[],
      step:0,
    }
  },
  methods:{
    /**
      Balance infos retrieved during the experiment and save it to db 
      Launch to next step
    */
    async add_step(json) {
      
      // init user welcome phase  
      if(this.step == 0){
        // init user Given Name
        this.user_name = json[0]['user_name'];
        //concat user info
        let user_info_concat = {
          "start_at":this.starting_date,
          "user_tech_config":Object.assign({}, this.user_ip_data, this.user_browser_data_auto, this.user_browser_data_manu),
          "language":this.$i18n.locale=="en" ? 0 : 1,
          "version":this.version,
          "scenes_order":this.scene_order,
          "answers_order":this.answer_order,
          "angles_order":this.scene_angles
        };
        //create user
        await this.createUser(this.id_poste,user_info_concat);
        //check error -> stop script

        this.step++;
        return;
      }
      //push json dbase
      if(this.step == 1){
        this.step++;
        return;
      }
      if(this.step == 2){
        this.given_answer = json;
        this.step++;
        return;
      }
      if(this.step == 4){
        return
      }
    },
    /**
      Create new user *POST*
    */
    async createUser(guid,data) {
      // Get config from back end
      let url = GConfig.URL_BACKEND + GConfig.URL_POSTDATA + guid;
      try{
        //Request
        let response = await axios.post(url, data);
        return response.data;
      }catch(err) {
        //reset step
        alert(this.$i18n.t('err_create_user'));
        location.reload(); 
        return false;
      }
    },
    /**
      Send data to db *PUT*
    */
    async save_data(data) {
      console.log("saved:",data)
      // Get config from back end
      let path = GConfig.URL_BACKEND + GConfig.URL_POSTDATA + this.id_poste;
      try{
        //Request
        let response = await axios.put(path,data);
        return response.data;
      }catch(err) {
        console.log(err);     
      }
    },
    /**
      Create random Guid
    */
    uuidv4() {
      return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c => (
        c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
      );
    },
    /**
      Shuffle an array via Fisher-Yates algorithm
    */
    shuffle(array) {
      var currentIndex = array.length, temporaryValue, randomIndex;

      // While there remain elements to shuffle...
      while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
      }
      return array;
    },
    /**
      Get info from user ip
    */
    async getip(){
      try{
        let response = await axios.get('https://ipinfo.io?token='+GConfig.IP_INFO_TOKEN+'&format=json');
        return response.data;
      }catch(err){
        console.log(err)
      }
    },
    /**
      Collect user infos and init user variables
    */
    init_userinfo(){
      //set ip
      this.getip().then(data=>{
        this.user_ip_data = data;
      });
      //set browser info 
      this.user_browser_data_auto= browserInfo.getBrowser();
      //set additional information
      this.user_browser_data_manu = {
        "app_version":navigator.appVersion,
        "app_code_Name":navigator.appCodeName,
        "platform":navigator.platform,
        "window_width":innerWidth,
        "window_height":innerHeight
      }
    },
    /**
      Create ramdomized user config
    */
    init_user_configs(){
      //setup random config
      this.scene_order = this.shuffle(this.scene_order);
        // ADD last scene
      this.scene_order.push(4,5);
      //setup random config
      this.answer_order = this.shuffle(this.answer_order);
      //setup random angles
      this.add_scene_angles()
      this.scene_angles = this.shuffle(this.scene_angles);
        // ADD last angles UP
      this.scene_angles.push([(40 + Math.random() * 5) * Math.PI/180, Math.random() * 360 * Math.PI/180]); 
    },
    /**
      Create ramdomized angles for the camera's starting point in the scenes 
    */
    add_scene_angles(){
      //get twice angles from 0-5
      for(let i=0;i<2;i++){
        // 0-5 + 0-360 in rad
        this.scene_angles.push([Math.random() * 5 * Math.PI/180, Math.random() * 360 * Math.PI/180]); 
      }
      //get twice angles from 40-45
      for(let i=0;i<2;i++){
        // 0-5 + 0-360 in rad
        this.scene_angles.push([(40 + Math.random() * 5) * Math.PI/180, Math.random() * 360 * Math.PI/180]); 
      } 
    }
  },

  //** INIT **//
  mounted(){    
    //set default language
    this.$i18n.locale = "en"
    //set id
    this.id_poste = this.uuidv4();
    //set date
    this.starting_date = new Date()
    // collect user info 
    this.init_userinfo()
    // init user configs
    this.init_user_configs()
  }
}
</script>

<style>
.sub-question{
  text-align:left;
  margin-bottom:2%;
  margin-left:1%;
  font: 30px 'Arial Narrow', sans-serif;
  color: #4CB27D;
}
.stage-size{
  margin:auto;
  width:60%;
  margin-top:3%;
  position: relative;
}
.Maintitle{
  top:0.5%;
  font: 35px 'Arial Narrow', sans-serif;
  color: #147e09;
  text-transform: uppercase;
  letter-spacing: -2px;
  position: relative;
}
.questiontitle{
  text-align:left;
  margin-left:1%;
  margin-bottom:2%;
  font: 30px 'Arial Narrow', sans-serif;
  color: #147e09;
}
.mb-2{
  margin-top:3%;
  margin-bottom:2%;
  position: relative;
}
.pl-2{
  padding-left:2%;
  position: absolute;
}
.b-2{
  margin-bottom:2%;
}
.error{
  color: #CC0000;
}
.valid{
  color: #000000;
}
.paragraph-text{
  text-align:left;
  margin-top:1%;
  margin-left:1%;
  font: 25px 'Arial Narrow', sans-serif;
}
.errnotif-position{
  position: fixed !important;
  z-index: 10;
  left: 30%;
  bottom: 2%;
  width:40%;
}
.notif-position{
  position: fixed !important;
  z-index: 10;
  right: 1%;
  top: 1%;
  width:30%;
}
</style>
