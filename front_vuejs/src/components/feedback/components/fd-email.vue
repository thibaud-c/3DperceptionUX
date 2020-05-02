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
  #rootEmail
    followup(v-if="em_step==0" @nextfeedem="nextquestion")
    mail(v-if="em_step==1" @nextfeedem="nextquestion")
</template>

<script>
import followup from './micro-cpt/micro-email-followup.vue'
import mail from './micro-cpt/micro-email-mail.vue'


export default {
  name: 'fd-email',
  components : { 
    followup,
    mail
  },
  data () {
    return {
      em_step:0,
      json_answer:{}
    }
  },
  methods: {
    nextquestion(data){
      // save location and add step if needed
      if(this.em_step==0){
        this.json_answer["followup"] = data[0];
        if(!data[1]){
          this.em_step++;
          return;
        }
        //don't do next step
        this.em_step+=2;
      }
      if(this.em_step==1){
        this.json_answer["email"] = data;
      }
      //save and pass next question
      this.$emit('nextfeedstep',this.json_answer);
    },
  }
}
</script>

<style>
</style>