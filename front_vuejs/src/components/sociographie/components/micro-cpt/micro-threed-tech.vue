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
  #rootM3D_T
    //TECH
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold(v-html="$t('socio-3d-questionTech')")
    label.checkbox.pl-2.b-2(v-if="!refus" v-for="tech,index in techAnswers" :class="valid?'valid':'error'")
      input(v-model="checkedtech" :value='index' :name="tech" type='checkbox' @change="reseterror()") 
      |   {{ $t(tech) }}   
    //no answer
    br
    label.checkbox
      input(v-model="refus" name="refuschecked" type='checkbox' @change="isrefus();reseterror()") 
      |   {{ $t("reponse-refus") }}         
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-threed-tech',
  data () {
    return {
      checkedtech:[],
      techAnswers:["socio-3d-tech-jeux", "socio-3d-tech-dessin", "socio-3d-tech-apps", "socio-3d-tech-earth", "socio-3d-tech-movies", "socio-3d-tech-vr", "socio-3d-tech-ar","reponse-autre"],
      valid:true,
      refus:false
    }
  },
  methods: {
    nextquestion(){
      if(!this.validate()){ return; }
      if(this.refus){this.checkedtech = [this.techAnswers.length]}
      let nextstep = false;
      if(this.checkedtech.indexOf(this.techAnswers.length-1)!=-1){
        nextstep = true;
      }
      this.$emit('nextthreed',[this.checkedtech,nextstep]);
    },
    validate(){
      if(this.checkedtech.length==0 && !this.refus){
        this.valid=false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid=true;
    },
    isrefus(){
      this.checkedtech=[];
    },
  }
}
</script>

<style>
</style>