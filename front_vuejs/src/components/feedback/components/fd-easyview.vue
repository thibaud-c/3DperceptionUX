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
  #rootEasyviews
    easiest(v-if="di_step==0" @nexteaseview="nextquestion")
    hardest(v-if="di_step==1" @nexteaseview="nextquestion")
</template>

<script>
import easiest from './micro-cpt/micro-pref-easy.vue'
import hardest from './micro-cpt/micro-pref-hard.vue'

export default {
  name: 'fd-easyviews',
  components : { 
    easiest,
    hardest
  },
  data () {
    return {
      di_step:0,
      json_answer:{}
    }
  },
  methods: {
    nextquestion(data){
      // save location and add step if needed
      if(this.di_step==0){
        this.json_answer["easy_scene"] = data;
        this.di_step++;
        return;
      }
      if(this.di_step==1){
        this.json_answer["hard_scene"] = data;
      }

      //save and pass next question
      this.$emit('nextfeedstep',this.json_answer);
    },
  }
}
</script>

<style>
</style>