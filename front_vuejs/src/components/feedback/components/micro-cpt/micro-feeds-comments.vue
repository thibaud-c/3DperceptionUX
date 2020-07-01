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
    // ERR Notif
    .notification.errnotif-position.is-danger.is-light(v-if="!valid")
      button.delete(@click="valid=true")
      span {{err_message}}
    // TITLE
    p.questiontitle.has-text-weight-semibold {{ $t('feed-co-question') }}
    //input
    .control.com-feed(v-if="!refus")
      textarea.textarea.b-2(type='textarea' rows="10" v-model='comment' :placeholder="' '+$t('holder-precision')" :class="valid?'':'is-danger'" @change="reseterror")
    span.left-position(v-if="!refus") {{charactersLeft}} / 1000
    br
    //refus
    label.checkbox.pl-2
      input(v-model="refus" name="edocheck" type='checkbox' @change="isrefus(),reseterror()") 
      |   {{ $t("reponse-refus") }}
    //validation
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(ref="nextB" @click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'micro-feeds-com',
  data () {
    return {
      comment:"",
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
      if(this.refus){this.comment=-0;}
      //save and pass next question
      this.$emit('nextfeedxp',this.comment);
      //remove button listerner
      s_methods.remove_entertonext()
    },
    /**
   * Validation ok the solution -> need one selected
   */
    validate(){
      //no numbers & no empty
      if(!this.refus && (this.comment==='')){
        this.valid = false;
        this.err_message=this.$i18n.t('err_no_selection');
        return false;
      }
      // > 1000 chars
      if(!this.refus && (this.comment.length>1000)){
        this.valid = false;
        this.err_message=this.$i18n.t('err_too_much_char');
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
     * Reset doesn't wants to add something
     */
    isrefus(){
      this.comment='';
    },
  },
  mounted(){
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)
  },
  computed: {
    charactersLeft() {
      let char = this.comment.length;
      return char;
    }
  }
}
</script>

<style>
.com-feed{
    width:80%;
    margin:auto !important;
}
.left-position{
  margin:auto;
  right:10%;
  position:absolute;
  font: 5px;
  color: #222222;
}
</style>