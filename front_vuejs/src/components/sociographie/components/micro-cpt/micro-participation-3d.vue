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
  #rootMDP_3d
    //Participation
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold(v-html="$t('socio-dp-3d')")
    //participation loop
    label.radio.pl-2(v-for="dp,id in hasparticipate" :class="valid?'valid':'error'")
      input(v-model='attendance3d' type='radio' :value='id' @change="reseterror") 
      |   {{ $t(dp) }}
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-pa-3d',
  data () {
    return {
      attendance3d:null,
      hasparticipate:["reponse-oui","reponse-non","reponse-forget","reponse-refus"],
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      //save and pass next question
      this.$emit('nextparticipation',this.attendance3d);
    },
    validate(){
      if(this.attendance3d===null){
        this.valid=false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid=true;
    }
  }
}
</script>

<style>
</style>