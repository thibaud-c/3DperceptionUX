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
    #rootMIMGDensity
      // country
      p.questiontitle.has-text-weight-semibold {{ $t('perc-lod-density') }}
      img.size-scene-density(:src="'perception/lod/'+conf[0]+'.png'")
      img.size-scene-density.separate-pics(:src="'perception/lod/'+conf[1]+'.png'")
      br.b-2
      label.radio.pl-2(v-for="de,id in densities" :class="valid?'valid':'error'")
          input(v-model='scene' type='radio' :value='id' name='denseradio' @change="reseterror") 
          |    {{ $t(de) }}
      #sub-btn.mb-2
        //button.button.is-text(@click='') {{ $t('btn-previous') }}
        button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'lod-micro-ima-density',
  props:['conf'],
  data () {
    return {
      scene:null,
      densities:['perc-lod-density-left', 'perc-lod-density-none', 'perc-lod-density-right', 'reponse-no-answer'],
      valid:true,
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      let result = this.mapping_scene()
      //save and pass next question
      this.$emit('nextlod',result);
    },
    mapping_scene(){
      // Map the answer to take into account the config
      switch(this.scene){
        case 0 :
          return this.conf[0]
        case 1 :
          return 2
        case 2 :
          return this.conf[1]
        case 3 :
          return 3
      } 
    },
    validate(){
      //if checked
      if(this.scene===null){
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
.size-scene-density{
    height:250px;
    width:250px;
    margin:auto;
}
.separate-pics{
    margin-left:50px;
}
</style>