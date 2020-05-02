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
    p.questiontitle.has-text-weight-semibold {{ $t('feed-hv-question') }}
    label.radio.pl-2.b-2(v-for="img,id in srcsolution" :class="valid?'valid':'error'")
        input(v-model='solution' type='radio' :value='id' @change="reseterror") 
        img.pl-2.image-easy-size(:src="'perception/'+img+'.png'")
    label.radio.pl-2(:class="valid?'valid':'error'")
        input(v-model='solution' type='radio' :value='srcsolution.length' @change="reseterror") 
        |    {{ $t('reponse-no-none') }}
    #sub-btn.mb-2
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'sd-vizthreed',
  data () {
    return {
      srcsolution:["lod/0","lod/1","style/2","style/3","style/4","style/5"],
      solution:"",
      valid:true
    }
  },
  methods: {
    nextquestion(){
      // aimed answer -> 2
      if(!this.validate()){ return; }
      this.$emit('nexteaseview',this.solution);
    },
    validate(){
      if(this.solution===""){
        this.valid=false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid=true;
    },
  }
}
</script>

<style>
.image-easy-size{
    height:250px;
    width:250px;
    margin:auto;
}
</style>