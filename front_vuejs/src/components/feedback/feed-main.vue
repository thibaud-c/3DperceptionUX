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
    intro(v-if="step==0" :user_name="user_name" @nextfeedstep="addStep" @save_db="send_data")
    buldingnb(v-if="step==1" @nextfeedstep="addStep" @save_db="send_data")
    feedbacks(v-if="step==2"  @nextfeedstep="addStep" @save_db="send_data")
    email(v-if="step==3" @nextfeedstep="addStep" @save_db="send_data")
    thankyou(v-if="step==4" :results="results" @nextfeedstep="addStep" @save_db="send_data")
</template>

<script>
import intro from './components/fd-introduction.vue'
import buldingnb from './components/micro-cpt/micro-nbbuildings.vue'
import feedbacks from './components/fd-feeds.vue'
import email from './components/fd-email.vue'
import thankyou from './components/fd-thankyou.vue'

export default {
  name: 'feedback',
  props: ["user_name","results"],
  components : { 
    // liste des composants utilisés dans la div principale
    intro,
    buldingnb,
    feedbacks,
    email,
    thankyou,
  },
  data () {
    return {
      step:0
    }
  },
  methods: {
    /**
     * step handler
     */
    addStep(){
      this.step++;
      if(this.step>3){
        //save database and pass next stage
        this.$emit('nextstage');
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
</style>