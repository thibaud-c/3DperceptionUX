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
  #rootMDP_T
    //Participation
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold(v-html="$t('socio-dp-sujet')")
    label.checkbox.pl-2.b-2(v-if="!refus" v-for="rol,index in role_answers" :class="valid?'valid':'error'")
      input(v-model="role" :value='index' :name="rol" type='checkbox' @change="reseterror()") 
      |   {{ $t(rol) }}   
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
  name: 'sd-grew',
  data () {
    return {
      attendancedp:null,
      numberattended:null,
      isOther:false,
      role:null,
      sujet:null,
      hasparticipate:["reponse-oui","reponse-non","reponse-refus"],
      nbParticipation:["socio-dp-nb1","socio-dp-nb1+","socio-dp-nb5+","socio-dp-nb10+"],
      valid:true,
      validR:true,
      validT:true,
      validN:true,
    }
  },
  methods: {
    updateValues(){
      this.isOther = false;
      if(this.attendancedp==0){
        this.isOther = true;
      }
      this.role=null;
      this.sujet=null;
      this.numberattended=null;
    },
    nextquestion(){
      if(!this.validate()){ return; }
      let json_answer = {"participation": this.attendancedp};
      if(this.attendancedp == 0){
        json_answer["participation-role"] = this.role;
        json_answer["participation-sujet"] = this.sujet;
        json_answer["participation-nombre"] = this.numberattended;
      }
      this.$emit('nextsociostep',json_answer);
    },
    validate(){
      if(this.attendancedp===null){
        this.valid=false;
        return false;
      }
      if(this.attendancedp===0){
        if(this.role===null || this.role===''){
          this.validR=false;
          return false;
        }
        if(this.sujet===null || this.sujet===''){
          this.validT=false;
          return false;
        }
        if(this.numberattended===null){
          this.validN=false;
          return false;
        }
      }
      return true;
    },
    razerror(){
      this.valid=true;
      this.validR=true;
      this.validT=true;
      this.validN=true;
    }
  }
}
</script>

<style>
</style>