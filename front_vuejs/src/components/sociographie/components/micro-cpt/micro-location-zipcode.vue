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
  #rootSD_L_MZ
    // Zip code / NPA
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold {{ npa_cp==0?$t('socio-lo-questionCP'):$t('socio-lo-questionNPA') }}
    .control.cpt-20.b-2(v-if="!refus") 
      input.input( type='text' v-model='codepost' :placeholder="npa_cp==0?'00000':'0000'" :class="valid?'':'is-danger'" @change="reseterror")
    //refus
    label.checkbox.pl-2
      input(v-model="refus" name="lozcheck" type='checkbox' @change="isrefus(),reseterror()") 
      |   {{ $t("reponse-refus") }}
    //button
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'sd-location-micro-zip',
  props: {
    npa_cp:Number
  },
  data () {
    return {
      codepost:null,
      valid:true,
      refus:false
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      if(this.refus){this.codepost=0;}
      //save and pass next question
      this.$emit('nextlocation',this.codepost);
    },
    validate(){
      let er = /^-?[0-9]+$/;
      if(this.refus){return true;}
      //number and filling
      if((this.codepost === null || this.codepost==='' || !er.test(this.codepost))){
        this.valid = false;
        return false;
      }
      // NPA number and CP number
      if(this.codepost.length != 5 && this.npa_cp == 0 || this.codepost.length != 4 && this.npa_cp == 1){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    },
    isrefus(){
      this.codepost=null;
    },
  }
}
</script>

<style>
</style>