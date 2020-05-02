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
  #rootAP
    instruction(v-if="question==0" @nextpersstep="addStep")
    tuto(v-if="question==1" :models="config['lod']" :answers="config['answer']" @nextpersstep="addStep")
    letsgo(v-if="question==2" @nextpersstep="addStep")
    aplod(v-if="question==3" :models="config['lod']" :answers="config['answer']" @nextpersstep="addStep")
    apstyle(v-if="question==4" :models="config['style']" :answers="config['answer']" @nextpersstep="addStep")
</template>

<script>
import instruction from './components/ap-instruction.vue'
import letsgo from './components/ap-letsgo.vue'
import tuto from './components/ap-tutorial.vue'
import aplod from './components/ap-lod.vue'
import apstyle from './components/ap-style.vue'


export default {
  name: 'perception',
  props:["config"],
  components : { 
    // liste des composants utilisés dans la div principale
    instruction,
    letsgo,
    tuto,
    aplod,
    apstyle
  },
  data () {
    return {
      question:0,
      json_answer:[]
    }
  },
  methods: {
    addStep(answer){
      if (answer !== undefined) {
        this.json_answer.push(answer);
      }
      this.question++;
      if(this.question>4){
        this.$emit('nextstage',this.obj_affectation(this.json_answer));
      }
    },
    obj_affectation(non_formated_arr){
      let obj = {};
      non_formated_arr.forEach(a => {
        Object.assign(obj,a);
      })
      return obj;
    }
  }
}
</script>

<style>
.size-whichleafletmap{
  height:200px;
  width:300px;
  margin:auto;
}
.size-leaflet{
  height:500px !important;
  width:550px !important;
  margin:auto;
}
.leaflet-container {
    background-color:rgba(255,0,0,0.0);
}
</style>