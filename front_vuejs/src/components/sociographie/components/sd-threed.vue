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
  #rootSD_3
    // TreeD
    treed(v-if="th_step==0" @nextthreed="nextquestion")
    treed_tech(v-if="th_step==1" @nextthreed="nextquestion")
    treed_tech_other(v-if="th_step==2" @nextthreed="nextquestion")
</template>

<script>
  import treed from './micro-cpt/micro-threed.vue'
  import treed_tech from './micro-cpt/micro-threed-tech.vue'
  import treed_tech_other from './micro-cpt/micro-threed-tech-other.vue'

  export default {
    name: 'sd-threed',
    components : { 
      treed,
      treed_tech,
      treed_tech_other
    },
    data () {
      return {
        th_step:0,
        json_answer:{}
      }
    },
    methods: {
      nextquestion(data){
        // save Threed and add step if needed
        if(this.th_step==0){
          this.json_answer["frequency_3d"] = data[0];
          //next step needed?
          if(data[1]){
            this.th_step++;
            return;
          }
        }
        if(this.th_step==1){
          this.json_answer["technology_3d"] = data[0];
          //next step needed?
          if(data[1]){
            this.th_step++;
            return;
          }
        }
        if(this.th_step==2){
          this.json_answer["technology_3d_other"] = data;
        }
        //save and pass next question
        this.$emit('nextsociostep',this.json_answer);
      },
    }
  }
</script>

<style>
</style>