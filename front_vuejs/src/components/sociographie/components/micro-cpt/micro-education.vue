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
  #rootMED
    //education 
    p.questiontitle.has-text-weight-semibold {{ $t('socio-ed-question') }}
    .select.b-2(v-if="!refus" :class="valid?'valid':'is-danger'")
      select(v-model="selected_education" @change='reseterror()')
        //education loop
        option.selected(:value="index" v-for="ed,index in education")
          p {{$t(ed)}} 
    br
    //refus
    label.checkbox.pl-2
      input(v-model="refus" name="edcheck" type='checkbox' @change="isrefus(),reseterror()") 
      |   {{ $t("reponse-refus") }}
    //validation
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-ed',
  data () {
    return {
      selected_education:null,
      education:["socio-ed-obligatoire","socio-ed-secondaire-prof","socio-ed-secondaire-général","socio-ed-sup-prof","socio-ed-sup-uni","reponse-autre"],
      refus:false,
      valid:true
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      //check if next step : Other
      let isOther = false;
      if(this.selected_education==this.education.length-1){isOther =true;}
      if(this.refus){this.selected_education = this.education.length}
      //save and pass next question
      this.$emit('nexteducation',[this.selected_education,isOther]);
    },
    validate(){
      // answer selected
      if(this.selected_education===null && !this.refus){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    },
    isrefus(){
      this.selected_education=null;
    },
  },
}
</script>

<style>
</style>