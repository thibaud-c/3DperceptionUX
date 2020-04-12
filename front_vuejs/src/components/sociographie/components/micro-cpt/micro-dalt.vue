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
  #rootDalt
    figure.image.image-dalt-size.b-2
      img(:src="image")
    #sub-dalt
      .control.cpt-20.b-2(v-if="!noNumber")
        input.input(type='text' v-model='chiffre' :placeholder="$t('socio-da-chiffreHold')" :class="valid?'':'is-danger'" @change="reseterror")
      label.checkbox.pl-2
        input(v-model="noNumber" name="checkbox" type='checkbox' @change="isnoNumber();reseterror()") 
        |   {{ $t("socio-da-noNumber") }}
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextdalt') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'sd-spatial',
  props:['image'],
  data () {
    return {
      noNumber:false,
      chiffre:null,
      valid:true
    }
  },
  methods: {
    isnoNumber(){
      this.chiffre="";
    },
    nextdalt(){
        if(!this.validate()){ return; }
        if(this.noNumber){this.chiffre=-0}
        this.$emit('nextdaltonism',this.chiffre);
        this.noNumber = '';
        this.chiffre = '';
    },
    validate(){
      if((this.chiffre===null || this.chiffre==="") && !this.noNumber){
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
.image-dalt-size{
    height:280px;
    width:280px;
    margin:auto;
}
</style>