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
  #rootEV-easy
    // ERR Notif
    .notification.errnotif-position.is-danger.is-light(v-if="!valid")
      button.delete(@click="valid=true")
      span {{err_message}}
    p.questiontitle.has-text-weight-semibold(v-html="$t('feed-hv-question')")
    label.radio.pl-2.b-2(v-for="img,id in srcsolution" :class="valid?'valid':'error'")
        input(v-model='solution' type='radio' :value='id' @change="reseterror") 
        img.image-easy-size(:src="'perception/'+img+'.png'")
    label.radio.pl-2(:class="valid?'valid':'error'")
        input(v-model='solution' type='radio' :value='srcsolution.length' @change="reseterror") 
        |    {{ $t('reponse-no-none') }}
    #sub-btn.mb-2
      button.button.is-primary(ref="nextB" @click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'ap-hardest-scene',
  data () {
    return {
      srcsolution:["exercices/0","exercices/1","exercices/2","exercices/3"],
      solution:"",
      err_message:"",
      valid:true
    }
  },
  methods: {
    /**
     * handle the next step process
     */
    nextquestion(){

      if(!this.validate()){ return; }
      this.$emit('nextlod',this.solution);
      //remove button listerner
      s_methods.remove_entertonext();
    },
    /**
     * Validation ok the solution -> need one selected
     */
    validate(){
      if(this.solution===""){
        this.valid=false;
        this.err_message=this.$i18n.t('err_no_selection');
        return false;
      }
      return true;
    },
    /**
     * Reset error
     */
    reseterror(){
      this.valid=true;
    },
  },
  mounted(){
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)
  }
}
</script>

<style>

</style>