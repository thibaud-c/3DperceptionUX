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
  #rootSD_G_MD
    // Density slider
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold {{ $t('socio-gr-densite') }}
    #sliderdensity(v-if="!refus") 
      output.output-gre-density(for='sliderWithValue') {{ $t(density) }}
      br
      span.slider-boundaries {{ $t('socio-lo-huntinghouse') }} ⊖
      input#sliderValued.slider.slider-size(v-model='density' min='1' :max='10' value='5' step='1' type='range')
      span.slider-boundaries ⊕ {{ $t('socio-lo-citycenter') }}
    //refus
    label.checkbox.pl-2
      input(v-model="refus" name="grdcheck" type='checkbox' @change="isrefus()") 
      |   {{ $t("reponse-refus") }}
    //button
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'sd-grew-micro-dens',
  data () {
    return {
      density:5,
      refus:false
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      if(this.refus){this.density = -0}
      //save and pass next question
      this.$emit('nextgrew',this.density);
    },
    validate(){
      return true;
    },
    isrefus(){
      this.density=5;
    },
  }
}
</script>

<style>
.output-gre-density{
  font: 25px 'Arial Narrow', sans-serif !important;
  padding: 5px 15px 5px 15px;
  border-radius: 10px 20px 10px 20px;
  font-weight: bold;
  background-color: #696969;
  color: white;
}
</style>