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
    // Difficulties comparison
    p.questiontitle.has-text-weight-semibold.b-2 {{ $t('perc-sta-perf') }}
    #diff(v-if="!refus")
      output.b-2.outputfreq(for='sliderWithValue') {{ $t(diffs[diff]) }}
      br.b-2
      span.slider-boundaries {{ $t('perc-mem-perf---') }} ⊖
      input.slider.slider-size(v-model='diff' min='0' max='4' value='2' step='1' type='range')
      span.slider-boundaries ⊕ {{ $t('perc-mem-perf-++') }}
    //no answer
    label.checkbox
      input(v-model="refus" name="checkbox" type='checkbox' @change="isrefus") 
      |   {{ $t("reponse-refus") }}   
    #sub-btn.mb-2
      button.button.is-primary(ref="nextB" @click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'micro-perf-mem-diff',
  data () {
    return {
      diff:2,
      diffs:["perc-mem-perf---", "perc-mem-perf--", "perc-mem-perf-=", "perc-mem-perf-+", "perc-mem-perf-++"],
      refus:false,
      valid:true
    }
  },
  methods: {
      /**
     * Get answer and send to next
     */
    nextquestion(){
      if(!this.validate()){ return; }
      if(this.refus){
          //if no answer -> and likert
        this.diff = this.diffs.length+1;
      }
      this.$emit('nextstat',this.diff);
      //remove button listerner
      s_methods.remove_entertonext();
    },
    /**
     * Check if the answer is correct
     */
    validate(){
      return true;
    },
    /**
     * Reset error handler
     */
    razerror(){
      this.valid=true;
    },    
    /**
     * Hide div if doesn't want to answer
     */
    isrefus(){
      this.diff=2;
    },
  },
  mounted(){
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)
  }
}
</script>

<style>
</style>