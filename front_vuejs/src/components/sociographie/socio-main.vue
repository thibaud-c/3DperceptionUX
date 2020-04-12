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
  #rootSocio
    instruction(v-if="question==0" @nextsociostep="addQuestion")
    genre(v-if="question==1" @nextsociostep="addQuestion")
    age(v-if="question==2" @nextsociostep="addQuestion")
    education(v-if="question==3" @nextsociostep="addQuestion")
    location(v-if="question==4" @nextsociostep="addQuestion")
    grew(v-if="question==5" @nextsociostep="addQuestion")
    threed(v-if="question==6" @nextsociostep="addQuestion")
    participation(v-if="question==7" @nextsociostep="addQuestion")
    daltonien(v-if="question==8" @nextsociostep="addQuestion")
    spatial(v-if="question==9" @nextsociostep="addQuestion")
    vizthreed(v-if="question==10" @nextsociostep="addQuestion")
</template>

<script>
import instruction from './components/sd-instruction.vue'
import genre from './components/sd-genre.vue'
import age from './components/sd-age.vue'
import education from './components/sd-education.vue'
import location from './components/sd-location.vue'
import grew from './components/sd-grew.vue'
import threed from './components/sd-threed.vue'
import participation from './components/sd-participation.vue'
import daltonien from './components/sd-daltonien.vue'
import spatial from './components/sd-spatial.vue'
import vizthreed from './components/sd-vizthreed.vue'

export default {
  name: 'sociodemography',
  components : {
    // liste des composants utilisés dans la div principale
    instruction,
    genre,
    age,
    education,
    location,
    grew,
    threed,
    participation,
    daltonien,
    spatial,
    vizthreed
  },
  data () {
    return {
      question:0,
      json_answer:[]
    }
  },
  methods: {
    //add the answer and launch next question
    addQuestion(answer){
      if (answer !== undefined) {
        this.json_answer.push(answer);
      }
      this.question++;
      if(this.question>10){
        //formalize json_answer
        let organized_answer = this.obj_affectation(this.json_answer);
        //save database and pass next stage
        this.$emit('nextstage',organized_answer);
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
.cpt-40{
  margin:auto;
  width:40%;
}
.cpt-20{
  margin:auto;
  width:20%;
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