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
  #rootFeeds
    globxp(v-if="xp_step==0" @nextfeedxp="nextquestion")
    dif(v-if="xp_step==1" @nextfeedxp="nextquestion")
    com(v-if="xp_step==2" @nextfeedxp="nextquestion")
</template>

<script>
import globxp from './micro-cpt/micro-feeds-globxp.vue'
import dif from './micro-cpt/micro-feeds-difficulty.vue'
import com from './micro-cpt/micro-feeds-comments.vue'

export default {
  name: 'fd-feeds',
  components : { 
    globxp,
    dif,
    com
  },
  data () {
    return {
      xp_step:0
    }
  },
  methods: {
    //next question
    nextquestion(data){
      
      /** Step handling **/

      if(this.xp_step==0){
        // Shape answer and send to db
        this.send("smile",data)
        this.xp_step++;
        return;
      }
      if(this.xp_step==1){
        this.send("difficulty",data)
        this.xp_step++;      
        return;
      }
      if(this.xp_step==2){
        this.send("comment",data)
      }
      //save and pass next question
      this.$emit('nextfeedstep',this.json_answer);
    },
      /**
     * Send data to db hadler
     */
    send(question_name,data_to_save){
      let json_answer = { [question_name] : data_to_save }
      this.$emit('save_db',json_answer);
    }
  }
}
</script>

<style>
</style>