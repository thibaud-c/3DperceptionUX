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
  #rootSD_G
    //grew
    gr(v-if="gr_step==0" @nextgrew="nextquestion")
    gr_zip(v-if="gr_step==1" @nextgrew="nextquestion" :npa_cp="json_answer['grew']")
    gr_dense(v-if="gr_step==2" @nextgrew="nextquestion")
</template>

<script>
import gr from './micro-cpt/micro-grew.vue'
import gr_zip from './micro-cpt/micro-grew-zipcode.vue'
import gr_dense from './micro-cpt/micro-grew-density.vue'

export default {
  name: 'sd-grew',
  components : { 
    gr,
    gr_zip,
    gr_dense
  },
  data () {
    return {
      gr_step:0,
      json_answer:{}
    }
  },
  methods: {
    nextquestion(data){
      console.log(data)
      // save location and add step if needed
      if(this.gr_step==0){
        this.json_answer["grew"] = data;
        this.gr_step++;
        // if refusal go to density
        if(data==3){this.gr_step=2}
        return;
      }
      if(this.gr_step==1){
        this.gr_step++;
        // context 0 -> cp / 1 -> country / 2 -> refusal
        if(data[1]==0){
          this.json_answer["grew_zipcode"] = data[0];
          return;
        }
        if(data[1]==1){
          this.json_answer["grew_country"] = data[0];
          return;
        }        
        return;
      }
      if(this.gr_step==2){
        this.json_answer["grew_density"] = data;
      }
      //save and pass next question
      this.$emit('nextsociostep',this.json_answer);
    },
  }
}
</script>

<style>
</style>