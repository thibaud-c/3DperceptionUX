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
  #rootEducation
    //education 
    ed(v-if="ed_step==0" @nexteducation="nextquestion")
    ed_other(v-if="ed_step==1" @nexteducation="nextquestion")
</template>

<script>
import ed from './micro-cpt/micro-education.vue'
import ed_other from './micro-cpt/micro-education-other.vue'

export default {
  name: 'sd-education',
  components : { 
    ed,
    ed_other
  },
  data () {
    return {
      ed_step:0,
      json_answer:{}
    }
  },
  methods: {
    nextquestion(data){
      // save education and add step if needed
      if(this.ed_step==1){
        this.json_answer["education_other"] = data;
      }
      if(this.ed_step==0){
        this.json_answer["education"] = data[0];
        if(data[1]){
          this.ed_step++;
          return;
        }
      }
      //save and pass next question
      this.$emit('nextsociostep',this.json_answer);
    },
  },
}
</script>

<style>
</style>