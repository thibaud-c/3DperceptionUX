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
  #rootFeed
    intro(v-if="step==0" @nextfeedstep="addStep")
    feedbacks(v-if="step==1" @nextfeedstep="addStep")
    email(v-if="step==2" @nextfeedstep="addStep")
    thankyou(v-if="step==3")
</template>

<script>
import intro from './components/fd-introduction.vue'
import feedbacks from './components/fd-feeds.vue'
import email from './components/fd-email.vue'
import thankyou from './components/fd-thankyou.vue'

export default {
  name: 'feedback',
  components : { 
    // liste des composants utilisés dans la div principale
    intro,
    feedbacks,
    email,
    thankyou
  },
  data () {
    return {
      step:0,
      json_answer:[]
    }
  },
  methods: {
    //add the answer and launch next step
    addStep(answer){
      if (answer !== undefined) {
        this.json_answer.push(answer);
      }
      this.step++;
      if(this.step>2){
        //save database and pass next stage
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
</style>