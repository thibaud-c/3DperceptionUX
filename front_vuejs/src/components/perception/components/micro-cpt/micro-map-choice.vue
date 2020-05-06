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
  #rootMIMGMAP
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold {{ $t('perc-lod-leaflet') }}
    label.radio.pl-2(v-for="img in answer_order" :class="valid?'valid':'error'")
      input(v-model='solution' type='radio' :value='img' name='imgmap' @change="reseterror") 
      img.b-2.size-whichleafletmap(:src="'perception/'+exercice+'/'+img+'.png'")
    br
    label.radio.pl-2(:class="valid?'valid':'error'")
      input(v-model='solution' type='radio' :value='answer_order.length' name='3dradio' @change="reseterror") 
      |   {{ $t('reponse-no-answer') }}
    #sub-btn.mb-2
      //button.button.is-text(@click="") {{ $t("btn-previous") }}
      button.button.is-primary(@click="nextquestion") {{ $t("btn-valider") }}
</template>

<script>

export default {
  name: 'lod-micro-ima-map',
  props:['answer_order','exercice'],
  data () {
    return {
        solution:null,
        valid:true,
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      let answer = [this.solution,true]
      if(this.solution==this.answer_order.length){answer[1]=false}
      this.$emit('nextlod',answer)
    },
    reseterror(){
        this.valid=true;
    },
    validate(){
      //if checked
      if(this.solution===null){
        this.valid = false;
        return false;
      }
      return true;
    },
  }
}
</script>

<style>
</style>