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
  #rootIC_FN
    // ERR Notif 
    .notification.errnotif-position.is-danger.is-light(v-if="!valid")
      button.delete(@click="valid=true")
      span {{err_message}}
    // title page
    p.questiontitle.has-text-weight-semibold {{ $t('intro-fn-question') }}
    //input poste
    .control.poste-20
      input.input.mtb-2(type='text' v-model='name' :placeholder="$t('intro-fn-holder')" :class="valid?'':'is-danger'" @change="reseterror")
    .sub-btns.mb-2
      button.button.is-success(ref="nextB" @click='nextquestion') {{ $t('btn-valider') }}

</template>

<script>
import s_methods from '../../../js/shared_methods.js'

export default {
  name: 'ic-forname',
  data () {
    return {
      name:"",
      valid:true,
      err_message:""
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      let json_answer = {"user_name":this.name}
      //save and pass next step
      this.$emit('nextintrostep', json_answer);
      //remove button listerner
      s_methods.remove_entertonext()
    },
    validate(){
      // check if not null
      if(!this.name){
        this.valid = false;
        this.err_message=this.$i18n.t('err_empty_field');
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    },
  },
  mounted(){
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)  
  }
}
</script>

<style>
.poste-20{
  margin:auto;
  width:20%;
}
</style>