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
    m_expl(v-if="memstep==0" :user_name="user_name" title="perc-mem-title" instruction="perc-mem-consigne" @nextmem="addStep")
    start(v-if="memstep==1" :step="17+memstep" :maxstep=27  @nextlod="addStep")
    m_mapchoice(v-if="memstep==2" :path="'exercices/'+scene" :view="views_config[models[scene]]" :answer='answers' :view_xy="angles[models[scene]]" @nextmem="addStep")
    m_tall(v-if="memstep==3" :path="'exercices/'+scene" :view="views_config[models[scene]]" :answer="answers" :view_xy="angles[models[scene]]" :footprint="'exercices/'+scene+'/'+map_selected" :l_data="views_config[models[scene]]['leaflet']" @nextmem="addStep")    
    m_pref(v-if="memstep==4" @nextmem="addStep")
</template>

<script>
import start from './micro-cpt/micro-per-start.vue'
import m_expl from './micro-cpt/micro-mem-explanation.vue'
import m_mapchoice from './micro-cpt/micro-mem-map-choice.vue'
import m_tall from './micro-cpt/micro-mem-tallest.vue'
import m_pref from './micro-cpt/micro-pref-memory.vue'

import views_config from './../../../assets/views.json'

export default {
  name: 'ap-mem',
  props:["models","answers","angles",'user_name'],
  components : { 
    // liste des composants utilisés dans la div principale
    start,
    m_expl,
    m_mapchoice,
    m_tall,
    m_pref
  },
  data () {
    return {
      memstep:0,
      scene:4,
      mod:0,
      views_config:"",
      map_selected:null,
      expected_answers:[1,2],
      given_answers:[]
    }

  },
  methods:{
    //next map
    addStep(data){
      // start
      if(this.memstep==0 || this.memstep==1){
        //next step
        this.memstep++;
        return;
      }

      /** Step handling **/

      //MAP
      if(this.memstep==2){
        this.map_selected = data["res"];
        // Save to user results
        this.given_answers.push(data["res"]);
        //no map selected -> get the good expected answer
        if(data["res"]==null){this.map_selected=this.expected_answers[4];}
        // Shape answer and send to db
        this.send("E4Q0",data)
        // next step
        this.memstep++;
        return;
      }

      //HEIGHT
      if(this.memstep==3){
        // Save to user results
        this.given_answers.push(data["res"]);
        // Shape answer and send to db
        this.send("E4Q1",data)
        this.memstep++;
        return;
      }

      //PREF
      if(this.memstep==4){
        // Shape answer and send to db
        this.send("pref_memory",data)
        this.memstep++;
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