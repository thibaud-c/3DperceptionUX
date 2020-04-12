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
    #rootMDE_P3d
      p.questiontitle.has-text-weight-semibold {{ $t('feed-p3-question') }}
      label.radio.pl-2(v-for="p3,id in part3ds" :class="valid?'valid':'error'")
          input(v-model='part3d' type='radio' :value='id' name='part3dradio' @change="reseterror") 
          |    {{ $t(p3) }}
      #sub-btn.mb-2
        //button.button.is-text(@click='') {{ $t('btn-previous') }}
        button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-fd-part3d',
  data () {
    return {
      part3d:null,
      part3ds:['feed-p3-0', 'feed-p3-1','feed-p3-2', 'feed-p3-3', 'feed-p3-4', 'reponse-no-opinion'],
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      //save and pass next question
      this.$emit('nextfeedxp',this.part3d);
    },
    validate(){
      //if checked
      if(this.part3d===null){
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
</style>