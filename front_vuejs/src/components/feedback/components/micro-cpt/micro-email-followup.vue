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
    #rootMDE_FU
      p.questiontitle.has-text-weight-semibold {{ $t('feed-em-question') }}
      label.radio.pl-2(v-for="fu,id in followups" :class="valid?'valid':'error'")
          input(v-model='fup' type='radio' :value='id' name='fupradio' @change="reseterror") 
          |    {{ $t(fu) }}
      #sub-btn.mb-2
        //button.button.is-text(@click='') {{ $t('btn-previous') }}
        button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-fd-email-fu',
  data () {
    return {
      fup:null,
      followups:['feed-em-results','feed-em-surveys', 'feed-em-interviews', 'feed-em-no', 'reponse-refus'],
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      let next = true;
      //Is next step
      if(this.fup<3){next=false}
      //save and pass next question
      this.$emit('nextfeedem',[this.fup,next]);
    },
    validate(){
      //if checked
      if(this.fup===null){
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
</style>