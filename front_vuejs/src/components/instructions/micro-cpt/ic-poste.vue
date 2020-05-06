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
  #rootIC_Po 
    p.questiontitle.has-text-weight-semibold {{ $t('intro-po-question') }}
    //input poste
    .control.poste-20
      input.input.mtb-2(type='text' v-model='place' :placeholder="$t('intro-po-holder')" :class="valid?'':'is-danger'" @change="reseterror")
    .sub-btns.mb-2
      label.checkbox.b-2
        input(v-model="isjump" name="sociocheck" type='checkbox') 
        |     {{ $t('btn-jump') }}
      br
      button.button.is-success(@click='nextquestion') {{ $t('btn-valider') }}
      br
</template>

<script>
export default {
  name: 'ic-poste',
  data () {
    return {
      place:"",
      valid:true,
      isjump:false
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      let json_answer = {"poste":this.place}
      //save and pass next step
      
      this.$emit('nextintrostep', [json_answer,this.isjump]);
    },
    validate(){
      let er = /^-?[0-9]+$/;
      // no letter & 2 numbers
      if(!er.test(this.place) /*|| this.place.length!=2*/){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    }
  }
}
</script>

<style>
.poste-20{
  margin:auto;
  width:20%;
}
</style>