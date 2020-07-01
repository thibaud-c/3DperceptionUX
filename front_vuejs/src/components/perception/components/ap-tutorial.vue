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
  #rootAP_T
    tutoExp(v-if="tutostep==0" :user_name="user_name" @nextlod="addStep")
    mapchoice(v-if="tutostep==1" path="tuto" :view="views_config['tuto']" :answer='[0,1,2]' :view_xy="angles" @nextlod="addStep")
    tall(v-if="tutostep==2" path="tuto" :view="views_config['tuto']" :view_xy="angles" footprint="tuto/0" :l_data="views_config['tuto']['leaflet']" @nextlod="addStep")
    views(v-if="tutostep==3" path="tuto" :view="views_config['tuto']" :view_xy="angles" @nextlod="addStep")
    results(v-if="tutostep==4" :result="checkresult()" @nextlod="addStep")
</template>

<script>
import tutoExp from './micro-cpt/micro-explanation.vue'
import mapchoice from './micro-cpt/micro-per-map-choice.vue'
import tall from './micro-cpt/micro-per-tallest.vue'
import views from './micro-cpt/micro-per-view.vue'
import results from './micro-cpt/micro-tuto-results.vue'

import views_config from './../../../assets/views.json'

export default {
  name: 'ap-tutorial',
  props:['user_name'],
  components : { 
    // liste des composants utilisés dans la div principale
    tutoExp,
    mapchoice,
    tall,
    views,
    results
  },
  data () {
    return {
      tutostep:0,
      expected_answers:[0,0,1],
      answers:[],
      angles:[],
      diff:[],
      start_time:null
    }
  },
  methods:{
    //next map
    addStep(answer){
      if (answer !== undefined) {
        //save answers
        this.answers.push(parseInt(answer['res']));
      }
      this.tutostep++;
      if (this.tutostep>4){
        // send time to db
        let json_answer = {"tuto_time":(new Date()).getTime() - this.start_time.getTime()};
        this.$emit('save_db',json_answer);
        
        /** Next stage **/
        this.$emit('nextpersstep');  
      }
    },
    /**
     * Calculate the success rate of the user on the exercice
     */
    checkresult(){
        // get difference with expected
        this.answers.forEach( (element,i) => { 
          this.diff[i] = this.expected_answers[i] == element
        });
        return Math.round(this.diff.filter( el => el ).length/this.diff.length*100)
       
    }
  },
  mounted(){
    // handle config for camera
    this.views_config = views_config;
    // initiate time counter 
    this.start_time = new Date();
    // Create camera random rotation
    this.angles = [Math.random() * 5 * Math.PI/180, Math.random() * 360 * Math.PI/180]

  }
}
</script>

<style>
</style>