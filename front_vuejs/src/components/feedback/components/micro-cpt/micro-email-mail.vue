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
  #rootMDE_MA
    // ERR Notif
    .notification.errnotif-position.is-danger.is-light(v-if="!valid")
      button.delete(@click="valid=true")
      span {{err_message}}
    //precision other
    p.questiontitle.has-text-weight-semibold {{ $t('feed-em-question+') }}
    //input
    .control.textarea-size.b-2(v-if="!refus") 
      input.input(type='text' v-model='email' :placeholder="$t('holder-precision')" :class="valid?'':'is-danger'" @change="reseterror")
    //refus
    label.checkbox.pl-2
      input(v-model="refus" type='checkbox' @change="isrefus(),reseterror()") 
      |   {{ $t("reponse-refus") }}
    //validation
    #sub-btn.mb-2
      button.button.is-primary(ref="nextB" @click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'micro-fd-email-ma',
  data () {
    return {
      email:null,
      refus:false,
      valid:true,
      err_message:"",
    }
  },
  methods: {
    /**
     * handle the next step process
     */
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      //if refus -> -0
      if(this.refus){this.email=-0;}
      //save and pass next question
      this.$emit('nextfeedem',this.email);
      //remove button listerner
      s_methods.remove_entertonext()
    },
    /**
     * Validation ok the solution -> need one selected
     */
    validate(){
      /* eslint-disable-next-line */
      let er = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      //no numbers & no empty
      if(!this.refus && !er.test(this.email)){
        this.valid = false;
        this.err_message=this.$i18n.t('err_not_email');
        return false;
      }
      return true;
    },
    /**
     * Reset error
     */
    reseterror(){
      this.valid = true;
    },
    /**
     * Handle don't want to gibe the email
     */
    isrefus(){
      this.email=null;
    },
  },
  mounted(){
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)
  }
}
</script>

<style>
.textarea-size{
  width:60%;
  margin:auto;
}
</style>