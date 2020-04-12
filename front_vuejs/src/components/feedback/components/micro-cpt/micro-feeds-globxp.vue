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
  #rootMF_GXP
    p.questiontitle.has-text-weight-semibold {{ $t('feed-xp-question') }}
    label.radio.pl-2(v-for="img,id in smiles" :class="valid?'valid':'error'")
      input(v-model='feed' type='radio' :value='id' name='smileradio' @change="reseterror") 
      img.feed-img-size(:src="'icons/'+img+'.png'")
    label.radio.pl-2(:class="valid?'valid':'error'")
      input(v-model='feed' type='radio' :value='smiles.length' name='smileradio' @change="reseterror") 
      |   {{ $t('reponse-refus') }}
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-feeds-globxp',
  data () {
    return {
      feed:null,
      smiles:['--','-', '=', '+', '++'],
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      //save and pass next question
      this.$emit('nextfeedxp',this.feed);
    },
    validate(){
      //if checked
      if(this.feed===null){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    }
  }
}
</script>

<style>
.feed-img-size{
    height:100px;
    width:100px;
}
</style>