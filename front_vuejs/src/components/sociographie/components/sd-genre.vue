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
  #rootGenre
    //Question
    p.questiontitle.has-text-weight-semibold {{ $t('socio-ge-question') }}
    //genders loop
    label.radio.pl-2(v-for="gender,id in genders" :class="valid?'valid':'error'")
      input(v-model='genre' type='radio' :value='id' name='genreradio' @change="reseterror") 
      |    {{ $t(gender) }}
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'sd-genre',
  data () {
    return {
      genre:null,
      genders:['socio-ge-masc','socio-ge-femi','reponse-refus'],
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      let json_answer = {"genre": this.genre};
      //save and pass next question
      this.$emit('nextsociostep',json_answer);
    },
    validate(){
      // check answer exist
      if(this.genre===null){
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