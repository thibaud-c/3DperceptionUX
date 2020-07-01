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
    tuto(v-if="question==1" :user_name="user_name" @save_db="send_data" @nextpersstep="addStep")
    letsgo(v-if="question==2" @nextpersstep="addStep")
    apperc(v-if="question==3" :models="scene_order" :answers="answer_order" :angles="scene_angles" @save_db="send_data" @nextpersstep="addStep")
    apmem(v-if="question==4" :user_name="user_name" :models="scene_order" :answers="answer_order" :angles="scene_angles" @save_db="send_data" @nextpersstep="addStep")
    apstat(v-if="question==5" :user_name="user_name" :models="scene_order" :answers="answer_order" :angles="scene_angles" @save_db="send_data" @nextpersstep="addStep")
</template>

<script>
import instruction from './components/ap-instruction.vue'
import tuto from './components/ap-tutorial.vue'
import letsgo from './components/ap-letsgo.vue'
import apperc from './components/ap-perception.vue'
import apmem from './components/ap-memory.vue'
import apstat from './components/ap-static.vue'


export default {
  name: 'perception',
  props:['user_name','scene_order','answer_order','scene_angles'],
  components : { 
    // liste des composants utilisés dans la div principale
    instruction,
    tuto,
    letsgo,
    apperc,
    apmem,
    apstat
  },
  data () {
    return {
      question:0,
      given_answers:[]
    }
  },
  methods: {
    /**
     * step handler
     */
    addStep(answer){
      if (answer !== undefined) {
        if(typeof answer[0][0] !== "undefined"){
          this.given_answers.push(...answer)
        }else{
          this.given_answers.push(answer)
        }
      }
      this.question++;
      if(this.question>5){
        this.$emit('nextstage',this.given_answers);
      }
    },
    /**
     * Senda data to db via PUT
     */
    send_data(answer){
      if (answer !== undefined) {
        this.$emit('send_data_to_db',answer);
      }
    }
  }
}
</script>

<style>
.column-size{
  position:relative;
  left:-25%;
  width:150%;
}
.size-threejs{
  height:75%;
  width:100%;
}
.column-center{
  vertical-align: middle;
  margin: auto;
}
.size-threejs{
  height:75%;
  width:100%;
}
.size-leaflet{
  height:50vh !important;
  width:40vw !important;
  margin:auto;
}
.leaflet-container {
    background-color:rgba(255,0,0,0.0);
}
.size-whichleafletmap{
  width:40%;
  margin:auto;
}
.outputfreq{
  font: 20px 'Arial Narrow', sans-serif !important;
  padding: 5px 15px 5px 15px;
  border-radius: 10px 20px 10px 20px;
  background-color: #696969;
  color: white;
}
.slider-boundaries{
  margin-right: .75rem;
  margin-left: .75rem;
  top: -1.25rem !important;
  position: relative;
  font-style: italic;
  font-weight: bold;
}
.slider-size{
  width:50% !important;
}
</style>