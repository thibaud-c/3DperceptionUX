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
  #rootSocio
    socio_par(v-if="question==0" :user_name="user_name" @nextsociostep="addQuestion")
    vizthreed(v-if="question==1" @nextsociostep="addQuestion")
</template>

<script>
import socio_par from './components/sd-socioparagraph.vue'
import vizthreed from './components/sd-vizthreed.vue'

export default {
  name: 'sociodemography',
  props:['user_name'],
  components : {
    // liste des composants utilisés dans la div principale
    socio_par,
    vizthreed
  },
  data () {
    return {
      question:0
    }
  },
  methods: {
    //add the answer and launch next question
    addQuestion(answer){
      if (answer !== undefined) {
        this.$emit('send_data_to_db',answer);
      }
      this.question++;
      if(this.question>1){
        //save database and pass next stage
        this.$emit('nextstage');
      }
    }
  }
}
</script>

<style>
</style>