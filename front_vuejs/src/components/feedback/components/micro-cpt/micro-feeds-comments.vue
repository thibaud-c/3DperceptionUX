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
  #rootMF_COM
    p.questiontitle.has-text-weight-semibold {{ $t('feed-co-question') }}
    //input
    .control.com-feed(v-if="!refus")
      textarea.textarea.b-2(type='textarea' rows="10" v-model='comment' :placeholder="' '+$t('holder-precision')" :class="valid?'':'is-danger'" @change="reseterror")
    //refus
    label.checkbox.pl-2
      input(v-model="refus" name="edocheck" type='checkbox' @change="isrefus(),reseterror()") 
      |   {{ $t("reponse-refus") }}
    //validation
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-feeds-com',
  data () {
    return {
      comment:null,
      refus:false,
      valid:true
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      //if refus -> -0
      if(this.refus){this.comment=-0;}
      //save and pass next question
      this.$emit('nextfeedxp',this.comment);
    },
    validate(){
      let er = /[^éèàùêîôâëïöç&'-_@$*,?;.:/!\w\s]/gi;
      //no numbers & no empty
      if(!this.refus && (this.comment ===null || this.comment==='') || er.test(this.comment)){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    },
    isrefus(){
      this.comment=null;
    },
  },
}
</script>

<style>
.com-feed{
    width:80%;
    margin:auto !important;
}
</style>