<!--
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
-->
<template lang="pug">
  #rootMEM
    s_expl(v-if="statstep==0" :user_name="user_name" title="perc-sta-title" instruction="perc-sta-consigne" @nextmem="addStep")
    start(v-if="statstep==1" :step="22+statstep" :maxstep=27  @nextlod="addStep")
    s_mapchoice(v-if="statstep==2" path="exercices/5" :view="views_config[models[5]]" :answer='answers' @nextstat="addStep")
    s_tall(v-if="statstep==3" path="exercices/5" :view="views_config[models[5]]" :answer="answers" :footprint="'exercices/5/'+map_selected" :l_data="views_config[models[5]]['leaflet']" @nextstat="addStep")    
    s_pref(v-if="statstep==4" @nextstat="addStep")
</template>

<script>
import start from './micro-cpt/micro-per-start.vue'
import s_expl from './micro-cpt/micro-mem-explanation.vue'
import s_mapchoice from './micro-cpt/micro-sta-map-choice.vue'
import s_tall from './micro-cpt/micro-sta-tallest.vue'
import s_pref from './micro-cpt/micro-pref-static.vue'

import views_config from './../../../assets/views.json'

export default {
  name: 'ap-sta',
  props:["models","answers","angles",'user_name'],
  components : { 
    // liste des composants utilisés dans la div principale
    start,
    s_expl,
    s_mapchoice,
    s_tall,
    s_pref
  },
  data () {
    return {
      statstep:0,
      views_config:"",
      map_selected:null,
      expected_answers:[2,2],
      given_answers:[]
    }

  },
  methods:{
    //next map
    addStep(data){
      // start
      if(this.statstep==0 || this.statstep==1){
        //next step
        this.statstep++;
        return;
      }

      /** Step handling **/

      //MAP
      if(this.statstep==2){
        this.map_selected = data["res"];
        // Save to user results
        this.given_answers.push(data["res"]);
        //no map selected -> get the good expected answer
        if(data["res"]==null){this.map_selected=this.expected_answers[4];}
        // Shape answer and send to db
        this.send("E5Q0",data)
        // next step
        this.statstep++;
        return;
      }

      //HEIGHT
      if(this.statstep==3){
        // Save to user results
        this.given_answers.push(data["res"]);
        // Shape answer and send to db
        this.send("E5Q1",data)
        this.statstep++;
        return;
      }

      //PREF
      if(this.statstep==4){
        // Shape answer and send to db
        this.send("pref_static",data)
        this.statstep++;
      }

      /** Next stage **/
      let success_rate = this.checkresult();
      this.$emit('nextpersstep',success_rate);
    },
      /**
     * Send data to db hadler
     */
    send(question_name,data_to_save){
      let json_answer = { [question_name] : data_to_save }
      this.$emit('save_db',json_answer);
    },
    /**
     * Check the results of the stage
     */
    checkresult(){
      let arr = []
      this.given_answers.forEach( (element,i) => { 
        arr[i] = this.expected_answers[i] == element
      });
      return arr;
    }
  },
  mounted(){
    this.views_config = views_config;
  }
}
</script>

<style>
</style>