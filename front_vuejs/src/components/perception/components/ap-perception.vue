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
  #rootPerc
    start(v-if="c1.includes(percstep)" :step="percstep" :maxstep=27  @nextlod="addStep")
    mapchoice(v-if="q1.includes(percstep)" :path="'exercices/'+models[mod]" :view="views_config[models[mod]]" :answer='answers' :view_xy="angles[models[mod]]" @nextlod="addStep")
    tall(v-if="q2.includes(percstep)" :path="'exercices/'+models[mod]" :view="views_config[models[mod]]" :answer='answers' :view_xy="angles[models[mod]]" :footprint="'exercices/'+models[mod]+'/'+map_selected" :l_data="views_config[models[mod]]['leaflet']" @nextlod="addStep")
    views(v-if="q3.includes(percstep)" :path="'exercices/'+models[mod]" :view="views_config[models[mod]]" :view_xy="angles[models[mod]]" @nextlod="addStep")
    low(v-if="q4.includes(percstep)" :path="'exercices/'+models[mod]" :view="views_config[models[mod]]" :answer='answers' :view_xy="angles[models[mod]]" :footprint="'exercices/'+models[mod]+'/'+map_selected" :l_data="views_config[models[mod]]['leaflet']" @nextlod="addStep")
    easiest(v-if="percstep==16" @nextlod="addStep")
    hardest(v-if="percstep==17" @nextlod="addStep")
</template>

<script>
import start from './micro-cpt/micro-per-start.vue'
import mapchoice from './micro-cpt/micro-per-map-choice.vue'
import tall from './micro-cpt/micro-per-tallest.vue'
import views from './micro-cpt/micro-per-view.vue'
import low from './micro-cpt/micro-per-lowest.vue'
import easiest from './micro-cpt/micro-pref-easy.vue'
import hardest from './micro-cpt/micro-pref-hard.vue'

import views_config from './../../../assets/views.json'

export default {
  name: 'ap-perc',
  props:["models","answers","angles"],
  components : { 
    // liste des composants utilisés dans la div principale
    start,
    mapchoice,
    tall,
    views,
    low,
    easiest,
    hardest
  },
  data () {
    return {
      percstep:0,
      mod:0,
      views_config:"",
      map_selected:null,
      expected_answers:[[0,2,1],[3,2,1],[0,2,3,8],[1,2,2,6]],
      given_answers:[[0,0,0],[0,0,0],[0,0,0,0],[0,0,0,0]],
      json_answer:{},
      c1:[0,4,8,12],
      q1:[1,5,9,13],
      q2:[2,6,10,14],
      q3:[3,7,11,15],
      q4:[104,108,112,116],
    }

  },
  methods:{
    //next map
    addStep(data){
      // start
      if(this.c1.includes(this.percstep)){
        //next step
        this.percstep++;
        //change model
        if(this.percstep>1){this.mod++}
        return;
      }

      /** Step handling **/

      //MAP
      if(this.q1.includes(this.percstep)){
        this.map_selected = data["res"];
        //no map selected -> get the good expected answer
        if(data["res"]==null){this.map_selected=this.expected_answers[this.models[[this.mod]]];}
        // Save to user results
        this.given_answers[this.models[[this.mod]]][0]=data["res"];
        // Shape answer and send to db
        this.send("E"+this.models[this.mod]+"Q0",data)
        // next step
        this.percstep++;
        return;
      }

      //HEIGHT TALL
      if(this.q2.includes(this.percstep)){
        // Save to user results
        this.given_answers[this.models[[this.mod]]][1]=data["res"];
        // Shape answer and send to db
        this.send("E"+this.models[this.mod]+"Q1",data)
        // next step
        this.percstep++;
        return;
      }

      //VIEW
      if(this.q3.includes(this.percstep)){
        if(this.models[this.mod]==2||this.models[this.mod]==3){
          // Scene 2 - 3 ask for lowest building
          this.percstep+=100;
        }
        // Save to user results
        this.given_answers[this.models[[this.mod]]][2]=data["res"];
        // Shape answer and send to db
        this.send("E"+this.models[this.mod]+"Q2",data)
        // next step
        this.percstep++;
        return;
      }

      //HEIGHT LOW
      if(this.q4.includes(this.percstep)){
        // Save to user results
        this.given_answers[this.models[[this.mod]]][3]=data["res"];
        // Shape answer and send to db
        this.send("E"+this.models[this.mod]+"Q3",data)
        // next step
        this.percstep-=100;
        return;
      }

      if(this.percstep==16){
        // Shape answer and send to db
        this.send("pref_easy",data)
        // next step
        this.percstep++;
        return;
      }
      if(this.percstep==17){
        // Shape answer and send to db
        this.send("pref_hard",data)
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
      let arr = [];
      this.expected_answers.forEach( (element,i)  => {
        let arr_bool = [];
        element.forEach( (el,j) => { 
          arr_bool[j] = parseInt(this.given_answers[i][j]) == parseInt(el);
        })
        arr.push(arr_bool)
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
.image-easy-size{
    width:20em;
    margin: auto;
    padding-left: 4px;
}
</style>