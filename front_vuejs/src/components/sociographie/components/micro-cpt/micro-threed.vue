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
  #rootM3D
    // TreeD
    p.questiontitle.has-text-weight-semibold {{ $t('socio-3d-question') }}
    #3d(v-if="!refus")      
      output.outputfreq(for='sliderWithValue') {{ $t(freqAnswers[frequecy3d]) }}
      br
      span.slider-boundaries {{ $t('socio-3d-jamais') }} ⊖
      input#sliderWithValue.slider.has-output.slider-size(v-model='frequecy3d' min='0' :max='5' value='3' step='1' type='range')
      span.slider-boundaries ⊕ {{ $t('socio-3d-quotidiennement') }}
    //no answer
    label.checkbox
      input(v-model="refus" name="checkbox" type='checkbox' @change="isrefus") 
      |   {{ $t("reponse-refus") }}   
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-threed',
  data () {
    return {
      frequecy3d:2,
      freqAnswers:["socio-3d-jamais", "socio-3d-rarement", "socio-3d-annuellement", "socio-3d-mensuellement", "socio-3d-hebdomadairement", "socio-3d-quotidiennement"],
      refus:false,
      valid:true
    }
  },
  methods: {
    nextquestion(){
      if(!this.validate()){ return; }
      if(this.refus){
        this.frequecy3d=this.freqAnswers.length;
      }
      //if next step
      let nextstep = false;
      if(this.frequecy3d != this.freqAnswers.length && this.frequecy3d > 2){
        nextstep = true;
      }
      this.$emit('nextthreed',[this.frequecy3d,nextstep]);
    },
    validate(){
      return true;
    },
    razerror(){
      this.valid=true;
    },    
    isrefus(){
      this.frequecy3d=2;
    },
  }
}
</script>

<style>
.outputfreq{
  font: 15px 'Arial Narrow', sans-serif !important;
  padding: 5px 15px 5px 15px;
  border-radius: 10px 20px 10px 20px;
  background-color: #696969;
  color: white;
}
</style>