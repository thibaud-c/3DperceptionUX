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
    #rootMIMGNbbuild
      // ERR Notif
      .notification.errnotif-position.is-danger.is-light(v-if="!valid")
        button.delete(@click="valid=true")
        span {{err_message}}
      //Nb Buildings 
      p.questiontitle.has-text-weight-semibold.b-2 {{ $t('perc-lod-buildings') }}
      label.radio.pl-2(v-for="nu,id in numbers" :class="valid?'valid':'error'")
          input(v-model='number' type='radio' :value='id' name='buildingsradio' @change="reseterror") 
          |    {{ $t(nu) }}
      #sub-btn.mb-2
        button.button.is-primary(ref="nextB" @click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'lod-micro-ima-nbbuildings',
  data () {
    return {
      number:null,
      numbers:['perc-lod-buildings-inf10', 'perc-lod-buildings-inf20', 'perc-lod-buildings-inf30', 'perc-lod-buildings-inf40', 'perc-lod-buildings-inf50', 'perc-lod-buildings-sup50', 'reponse-no-answer'],
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
      // Shape answer and send to db
      this.send("estim_building",this.number)
      // pass next question
      this.$emit('nextfeedstep');
      //remove button listerner
      s_methods.remove_entertonext()
    },
    /**
     * Validation ok the solution -> need one selected
     */
    validate(){
      //if checked
      if(this.number===null){
        this.valid = false;
        this.err_message=this.$i18n.t('err_no_selection');
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
     * Send data to db hadler
     */
    send(question_name,data_to_save){
      let json_answer = { [question_name] : data_to_save }
      this.$emit('save_db',json_answer);
    },
  },
  mounted(){
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)
  }
}
</script>

<style>
.size-scene-density{
    height:250px;
    width:250px;
    margin:auto;
}
.separate-pics{
    margin-left:50px;
}
</style>