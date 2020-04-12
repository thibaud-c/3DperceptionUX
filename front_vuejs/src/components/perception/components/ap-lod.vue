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
    start(v-if="c1.includes(lodstep)" @nextlod="addStep")
    three(v-if="c2.includes(lodstep)" :model="'perception/lod/'+models[mod]+'/3d.glb'" :view="views_config[models[mod]]" @nextlod="addStep")
    mapchoice(v-if="q1.includes(lodstep)" :conf="models[mod]" :answer_order='answers' @nextlod="addStep")
    leaflet(v-if="q2.includes(lodstep)" :footprint="'perception/lod/'+models[mod]+'/'+map_selected+'.geojson'" :center="views_config[models[mod]]['center']" :zoom="views_config[models[mod]]['zoom']" @nextlod="addStep")
    nbbuildings(v-if="bonusnb.includes(lodstep)" :conf="models" @nextlod="addStep")
    angleview(v-if="q3.includes(lodstep)" :conf="models[mod]" @nextlod="addStep")
    densitycomparison(v-if="lodstep==10" :conf="models" @nextlod="addStep")
</template>

<script>
import start from './micro-cpt/micro-start.vue'
import three from './micro-cpt/micro-three.vue'
import mapchoice from './micro-cpt/micro-map-choice.vue'
import leaflet from './micro-cpt/micro-leaflet.vue'
import angleview from './micro-cpt/micro-angleview.vue'
import nbbuildings from './micro-cpt/micro-nbbuildings.vue'
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
    leaflet,
    angleview,
    densitycomparison,
    nbbuildings
  },
  data () {
    return {
      lodstep:0,
      mod:0,
      views_config:"",
      map_selected:null,
      expected_answers:[0,2],
      json_answer:{},
      c1:[0,5],
      c2:[1,6],
      q1:[2,7],
      q2:[3,8],
      q3:[4,9],
      bonusnb:[104,105,109,110],
      time3d:null
    }

  },
  methods:{
    //next map
    addStep(data){
      /** Timer **/
      
      if(this.c1.includes(this.lodstep)){
        //start timer
        this.time3d = new Date();
        this.lodstep++;
        //change model
        if(this.lodstep>4){this.mod++}
        return;
      }
      if(this.c2.includes(this.lodstep)){
        //stop timer
        let difftime = new Date();
        var dif = difftime.getTime() - this.time3d.getTime();
        this.json_answer["E"+this.models[this.mod]+"Time"] = dif;
        this.lodstep++;
        return;
      }

      /** Step handling **/

      if(this.q1.includes(this.lodstep)){
        this.json_answer["E"+this.models[this.mod]+"Q0"] = data[0];
        this.map_selected = data[0];
        //no map selected -> get the good expected answer
        if(!data[1]){this.map_selected=this.expected_answers[this.models[[this.mod]]];}
        this.lodstep++;
        return;
      }

      if(this.q2.includes(this.lodstep)){
        this.json_answer["E"+this.models[this.mod]+"Q1"] = data;
        // Error in the map selected -> pass angle of view step
        if(this.map_selected!=this.expected_answers[this.models[[this.mod]]]){
          this.lodstep++;
        }
        if(this.models[this.mod]==1){
          //lod 2 -> ask nb of bulding
          this.lodstep+=100;
        }
        this.lodstep++;
        console.log(this.lodstep)
        return;
      }

      if(this.bonusnb.includes(this.lodstep)){
        this.json_answer["E1Q3"] = data;
        this.lodstep-=100;
        return;
      }

      if(this.q3.includes(this.lodstep)){
        this.json_answer["E"+this.models[this.mod]+"Q2"] = data;
        //change lod
        this.lodstep++;
        return;
      }

      if(this.lodstep==10){
        this.json_answer["E1Q4"] = data;
        this.lodstep++;
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
.size-whichleafletmap{
  height:200px;
  width:300px;
  margin:auto;
}

</style>