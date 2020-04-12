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
  #root_AV
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold {{ $t('perc-lod-view') }}
    img.size-angleview(:src="'perception/lod/'+conf+'/aov.png'")
    br
    label.radio.pl-2(v-for="view,id in views_possibility" :class="valid?'valid':'error'")
      input(v-model='user_answer' type='radio' :value='id' name='viewradio' @change="reseterror") 
      |    {{ $t(view) }}
    #sub-btn.mb-2
    //button.button.is-text(@click='') {{ $t('btn-previous') }}
    button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>

export default {
  name: 'lod-micro-views',
  props:['conf'],
  data () {
    return {
      user_answer:null,
      views_possibility:['perc-lod-view-rdc','perc-lod-view-mid', 'perc-lod-view-roof', 'perc-lod-view-none', 'reponse-no-answer'],
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      this.$emit('nextlod',this.user_answer)
    },
    reseterror(){
        this.valid=true;
    },
    validate(){
      //if checked
      if(this.user_answer===null){
        this.valid = false;
        return false;
      }
      return true;
    },
  }
}
</script>

<style>
.size-angleview{
    height:400px;
    width:400px;
    margin:auto;
}
</style>