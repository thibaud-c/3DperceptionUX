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
  #rootSD_P_MR_O
    // Tech other
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold {{ $t('socio-dp-role-other') }}
    //input
    .control.cpt-40.b-2(v-if="!refus") 
      input.input(type='text' v-model='role_other' :placeholder="$t('holder-precision')" :class="valid?'':'is-danger'" @change="reseterror()")
    //no answer
    label.checkbox
      input(v-model="refus" name="refuschecked" type='checkbox' @change="isrefus();reseterror()") 
      |   {{ $t("reponse-refus") }}    
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'sd-participation-micro-role-o',
  data () {
    return {
      refus:false,
      role_other:null,
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      if(!this.validate()){ return; }
      //if refus -> -0
      if(this.refus){this.role_other=-0;}
      //save and pass next question
      this.$emit('nextparticipation',this.role_other);
    },
    validate(){
      let er = /[^éèàùêîôâëïöç&'-_@$*,?;.:/!\w\s]/gi;
      //no numbers & no empty
      if(!this.refus && (this.role_other ===null || this.role_other==='') || er.test(this.role_other)){
        this.valid=false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid=true;
    },
    isrefus(){
      this.role_other=null;
    },
  }
}
</script>

<style>
</style>