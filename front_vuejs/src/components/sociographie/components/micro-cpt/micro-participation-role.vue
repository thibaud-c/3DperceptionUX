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
  #rootMDP_R
    //Participation
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold(v-html="$t('socio-dp-role')")
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
  name: 'sd-pa-ro',
  data () {
    return {
      role_answers:["socio-dp-role-participant", "socio-dp-role-observateur", "socio-dp-role-animateur", "socio-dp-role-association", "socio-dp-role-expert", "socio-dp-role-élu", "socio-dp-role-scribe","reponse-autre"],
      role:[],
      refus:false,
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      if(!this.validate()){ return; }
      if(this.refus){this.role = [this.role_answers.length]}
      let nextstep = false;
      if(this.role.indexOf(this.role_answers.length-1)!=-1){
        nextstep = true;
      }
      this.$emit('nextparticipation',[this.role,nextstep]);
    },
    validate(){
      if(this.role.length==0 && !this.refus){
        this.valid=false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid=true;
    },
    isrefus(){
      this.role=[];
    },
  }
}
</script>

<style>
</style>