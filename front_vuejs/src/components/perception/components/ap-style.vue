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
  #rootEx1
    start(v-if="c1.includes(stylestep)" @nextlod="addStep")
    three(v-if="c2.includes(stylestep)" :model="'perception/style/'+models[mod]+'/3d.glb'" :view="views_config[models[mod]]" @nextlod="addStep")
    nbbuildings(v-if="bonusnb.includes(stylestep)" :conf="models" @nextlod="addStep")    
    mapchoice(v-if="q1.includes(stylestep)" :exercice="'style/'+models[mod]" :answer_order='answers' @nextlod="addStep")
    memory(v-if="q2.includes(stylestep)" :exercice="'style/'+models[mod]" :answer_order='answers' :map="map_selected" @nextlod="addStep")
    leaflet(v-if="q3.includes(stylestep)" :footprint="'perception/style/'+models[mod]+'/'+map_selected+'.geojson'" :center="views_config[models[mod]]['center']" :zoom="views_config[models[mod]]['zoom']" @nextlod="addStep")
    lowerbati(v-if="q4.includes(stylestep)" :footprint="'perception/style/'+models[mod]+'/'+map_selected+'.geojson'" :center="views_config[models[mod]]['center']" :zoom="views_config[models[mod]]['zoom']" @nextlod="addStep")
    densitycomparison(v-if="stylestep==24" context="style" :conf="models" :available_answers="models.length" @nextlod="addStep")
</template>

<script>
import start from './micro-cpt/micro-start.vue'
import three from './micro-cpt/micro-three.vue'
import nbbuildings from './micro-cpt/micro-nbbuildings.vue'
import mapchoice from './micro-cpt/micro-map-choice.vue'
import memory from './micro-cpt/micro-memory.vue'
import leaflet from './micro-cpt/micro-leaflet.vue'
import lowerbati from './micro-cpt/micro-lowerbuildings.vue'
import densitycomparison from './micro-cpt/micro-densitycomparison.vue'

import views_config from './../../../assets/views.json'

export default {
  name: 'ap-lod',
  props:["models","answers"],
  components : { 
    // liste des composants utilisés dans la div principale
    start,
    three,
    mapchoice,
    memory,
    leaflet,
    lowerbati,
    densitycomparison,
    nbbuildings
  },
  data () {
    return {
      stylestep:0,
      mod:0,
      views_config:"",
      map_selected:null,
      expected_answers:[0,1,2,3,0,1],
      json_answer:{},
      c1:[0,6,12,18],
      c2:[1,7,13,19],
      q1:[2,8,14,20],
      q2:[3,9,15,21],
      q3:[4,10,16,22],
      q4:[5,11,17,23],
      bonusnb:[102,108,114,120],
      time3d:null
    }

  },
  methods:{
    //next map
    addStep(data){
      console.log(this.stylestep)
      /** Timer **/
      if(this.c1.includes(this.stylestep)){
        //start timer
        this.time3d = new Date();
        this.stylestep++;
        //change model
        if(this.stylestep>1){this.mod++}
        return;
      }
      if(this.c2.includes(this.stylestep)){
        //stop timer
        let difftime = new Date();
        var dif = difftime.getTime() - this.time3d.getTime();
        this.json_answer["E"+this.models[this.mod]+"Time"] = dif;
        this.json_answer["E"+this.models[this.mod]+"Inputs"] = data;
        if(this.models[this.mod]==3){
          //lod 2 -> ask nb of bulding
          this.stylestep+=100;
        }
        this.stylestep++;
        return;
      }

      /** Step handling **/

      //MAP
      if(this.q1.includes(this.stylestep)){
        this.json_answer["E"+this.models[this.mod]+"Q0"] = parseInt(data[0]);
        this.map_selected = data[0];
        //no map selected -> get the good expected answer
        if(!data[1]){this.map_selected=this.expected_answers[this.models[[this.mod]]]}
        
        this.stylestep++;
        return;
      }

      //HEIGHT
      if(this.q3.includes(this.stylestep)){
        this.json_answer["E"+this.models[this.mod]+"Q1"] = parseInt(data[0]);
        this.json_answer["E"+this.models[this.mod]+"Q1C"] = data[1];
        this.stylestep++;
        return;
      }

      //MEMORY
      if(this.q2.includes(this.stylestep)){
        this.json_answer["E"+this.models[this.mod]+"Q3"] = parseInt(data);
        this.stylestep++;
        return;
      }

      //VIEWS
      if(this.q4.includes(this.stylestep)){
        //TODO C
        let arrBuilding = [];
        let arrCoord = [];
        data.forEach(el => {
          arrBuilding.push(parseInt(el[0]));
          arrCoord.push(el[1]);
        });
        this.json_answer["E"+this.models[this.mod]+"Q2"] = arrBuilding;
        this.json_answer["E"+this.models[this.mod]+"Q2C"] = arrCoord;
        //change lod
        this.stylestep++;
        return;
      }

      if(this.bonusnb.includes(this.stylestep)){
        this.json_answer["E3Q4"] = parseInt(data);
        this.stylestep-=100;
        return;
      }

      if(this.stylestep==24){
        this.json_answer["E5Q5"] = data;
        this.stylestep++;
      }

      /** Next stage **/
      this.$emit('nextpersstep',this.json_answer);
    },
    razerror(){
      this.valid=true;
    }
  },
  mounted(){
    this.views_config = views_config;
  }
}
</script>

<style>
</style>