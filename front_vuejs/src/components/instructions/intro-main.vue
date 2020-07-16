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
  #rootIM
    welcome(v-if="step==0" @nextintrostep="addStep")
    plan(v-if="step==1" @nextintrostep="addStep")
    firstname(v-if="step==2" @nextintrostep="addStep")
    consentement(v-if="step==3" :user_name='json_answer[0]["user_name"]' @nextintrostep="addStep")
</template>

<script>
import welcome from './micro-cpt/ic-welcome.vue'
import plan from './micro-cpt/ic-planning.vue'
import firstname from './micro-cpt/ic-firstname.vue'
import consentement from './micro-cpt/ic-consentement.vue'

export default {
  name: 'introduction',
  components : { 
    // liste des composants utilisés dans la div principale
    welcome,
    plan,
    firstname,
    consentement
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
      if(this.step>3){
        //save database and pass next stage
        this.$emit('nextstage',this.json_answer);
      }
    }
  }
}
</script>

<style>
</style>