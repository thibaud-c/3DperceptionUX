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
    tutoExp(v-if="tutostep==0" @nextlod="addStep")
    start(v-if="tutostep==1" @nextlod="addStep")
    three(v-if="tutostep==2" model="perception/tuto/3d.glb" :view="views_config['tuto']" @nextlod="addStep")
    mapchoice(v-if="tutostep==3" exercice="tuto/" :answer_order='["0","1","2"]' @nextlod="addStep")
    leaflet(v-if="tutostep==4" :footprint="'perception/tuto/0.geojson'" :center="views_config['tuto']['center']" :zoom="views_config['tuto']['zoom']" @nextlod="addStep")
</template>

<script>
import tutoExp from './micro-cpt/micro-explanation.vue'
import start from './micro-cpt/micro-start.vue'
import three from './micro-cpt/micro-three.vue'
import mapchoice from './micro-cpt/micro-map-choice.vue'
import leaflet from './micro-cpt/micro-leaflet.vue'

import views_config from './../../../assets/views.json'

export default {
  name: 'ap-tutorial',
  components : { 
    // liste des composants utilisés dans la div principale
    tutoExp,
    start,
    three,
    mapchoice,
    leaflet,
  },
  data () {
    return {
      tutostep:0,
    }

  },
  methods:{
    //next map
    addStep(){
      this.tutostep++;
      if (this.tutostep>4){
        /** Next stage **/
        this.$emit('nextpersstep');
      }
    }
  },
  mounted(){
    this.views_config = views_config;
  }
}
</script>

<style>
</style>