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
  #rootSD_D
    //daltonien 
    p.questiontitle.has-text-weight-semibold {{ $t('socio-da-question') }}
    dalt(:image="images[stepDalt]" :answer="answers[stepDalt]" @nextdaltonism="nextdalt")
</template>

<script>
import dalt from './micro-cpt/micro-dalt.vue'

export default {
  name: 'sd-daltonien',
  components : { 
    dalt
  },
  data () {
    return {
      stepDalt:0,
      json_answer:{},
      answers:[45,3,42],
      images:['tests/dalt-dischromate.jpg','tests/datl-rouge-vert.jpg','tests/dalt-proto.jpg']
    }
  },
  methods: {
    nextdalt(daltnumber){
      if(this.stepDalt==0){
        this.json_answer["colorblind_dc"]=daltnumber;
      }else if(this.stepDalt==1){
        this.json_answer["colorblind_rg"]= daltnumber;
      }else if(this.stepDalt==2){
        this.json_answer["colorblind_pt"]= daltnumber;
      }
      this.stepDalt++;
      if(this.stepDalt>=this.images.length){
        this.$emit('nextsociostep',this.json_answer);
      }
    }
  }
}
</script>

<style>
</style>