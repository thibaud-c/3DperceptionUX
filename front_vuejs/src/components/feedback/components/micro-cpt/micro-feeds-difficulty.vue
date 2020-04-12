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
  #rootMF_DIF
    // TreeD
    p.questiontitle.has-text-weight-semibold {{ $t('feed-di-question') }}
    #3d(v-if="!refus")      
      span.slider-boundaries {{ $t('feed-di---') }} ⊖
      input.slider(v-model='diff' min='0' max='6' value='3' step='1' type='range')
      span.slider-boundaries ⊕ {{ $t('feed-di-++') }}
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
  name: 'micro-feeds-diff',
  data () {
    return {
      diff:3,
      refus:false,
      valid:true
    }
  },
  methods: {
    nextquestion(){
      if(!this.validate()){ return; }
      if(this.refus){
          //if no answer -> and likert
        this.diff=7;
      }
      this.$emit('nextfeedxp',this.diff);
    },
    validate(){
      return true;
    },
    razerror(){
      this.valid=true;
    },    
    isrefus(){
      this.diff=3;
    },
  }
}
</script>

<style>
</style>