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
    stepper(:steps.sync="step")
    .stage-size
      introWelcome(v-if="step==0" @nextstage="addAstep")
      introSocio(v-if="step==1" @nextstage="addAstep")
      perception(v-if="step==2" @nextstage="addAstep" :config="user_config")
      feedback(v-if="step==4" @nextstage="addAstep")
</template>
  
<script>
import axios from 'axios';
import GConfig from './../assets/config.json'
// pages imports
import stepper from './global/glob-stepper.vue'
import introWelcome from './instructions/intro-main.vue'
import introSocio from './sociographie/socio-main.vue'
import perception from './perception/perc-main.vue'
import feedback from './feedback/feed-main.vue'

export default {
  name: 'startsurvey',
  components : { 
    // liste des composants utilisés dans la div principale
    stepper,
    introWelcome,
    introSocio,
    perception,
    feedback
  },
  data () {
    return {
      id_poste:"",
      user_config:{},
      step:0,
    }
  },
  methods:{
    //get json from the stage -> send to database and launch next step
    async addAstep(json) {
      //Get user config from poste number && save poste config id 
      if(this.step == 0){
        this.id_poste = json[0][0]["poste"];
        this.user_config = await this.getConfig(this.id_poste);
        //check error -> stop script
        if(!this.user_config){return}
        if(json[0][1]){
          this.step+=2;
          return
        }
        this.step++;
        return;
      }
      //push json dbase
      if(this.step == 1){
        await this.savedata(this.id_poste,json);
        this.step++;
        return;
      }
      if(this.step == 2){
        await this.savedata(this.id_poste,json);
        this.step+=2;
        return;
      }
      if(this.step == 4){
        await this.savedata(this.id_poste,json);
      }
    },
    async getConfig(id) {
      // Get config from back end
      let path = GConfig.URL_BACKEND + GConfig.URL_GETCONFIG + id;
      try{
        //Request
        let response = await axios.get(path);
        return response.data;
      }catch(err) {
        this.step=0;
        console.error("id : ", this.id_poste, "//", err);
        //reset step
        alert(this.$i18n.t('Error-backend'));
        return false;
      }
    },
    async savedata(id,data) {
      console.log("saved:",data)
      // Get config from back end
      let path = GConfig.URL_BACKEND + GConfig.URL_SETANSWER + id;
      try{
        //Request
        let response = await axios.put(path,data);
        return response.data;
      }catch(err) {
        console.error("id : ", this.id_poste, "//", err);
        console.log("data : ", data)
        alert(this.$i18n.t('Error-backend'));
       
      }
    }
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
  font: 30px 'Arial Narrow', sans-serif;
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
  position: relative;
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
  font: 22px 'Arial Narrow', sans-serif;
}
</style>
