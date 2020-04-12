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
  #rootLocation
    // location
    lo(v-if="lo_step==0" @nextlocation="nextquestion")
    lo_zip(v-if="lo_step==1" @nextlocation="nextquestion" :npa_cp="json_answer['location']")
    lo_dense(v-if="lo_step==2" @nextlocation="nextquestion")
</template>

<script>
  import lo from './micro-cpt/micro-location.vue'
  import lo_zip from './micro-cpt/micro-location-zipcode.vue'
  import lo_dense from './micro-cpt/micro-location-density.vue'

  export default {
    name: 'sd-location',
    components : { 
      lo,
      lo_zip,
      lo_dense
    },
    data () {
      return {
        lo_step:0,
        json_answer:{}
      }
    },
    methods: {
      nextquestion(data){
        // save location and add step if needed
        if(this.lo_step==0){
          this.json_answer["location"] = data;
          this.lo_step++;
          // if refusal go to density
          if(data==2){this.lo_step=2}
          return;
        }
        if(this.lo_step==1){
          this.json_answer["location_zipcode"] = data;
          this.lo_step++;
          return;
        }
        if(this.lo_step==2){
          this.json_answer["location_density"] = data;
        }
        //save and pass next question
        this.$emit('nextsociostep',this.json_answer);
      },
    }
  }
</script>

<style>
</style>