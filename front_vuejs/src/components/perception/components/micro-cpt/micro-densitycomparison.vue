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
      p.questiontitle.has-text-weight-semibold(v-html="$t('perc-lod-density')")
      span(v-for="model in conf")
        img.size-scene-density.separate-pics(:src="'perception/'+context+'/'+model+'.png'")
      br.b-2
      label.checkbox.pl-2(v-for="ans in available_answers" :class="valid?'valid':'error'")
          input(v-model='scene' type='checkbox' :value='ans' name='denseradio' @change="reseterror") 
          |    {{ $t('perc-lod-density-'+ans) }}
          //no answer
      label.checkbox.pl-2(:class="valid?'valid':'error'")
        input(v-model="scene" name="refuschecked" type='checkbox' :value='0' @change="reseterror") 
        |   {{ $t("reponse-no-answer") }}     
      #sub-btn.mb-2
        //button.button.is-text(@click='') {{ $t('btn-previous') }}
        button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'lod-micro-ima-density',
  props:['conf','context','available_answers'],
  data () {
    return {
      scene:[],
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
      let result = []
      this.scene.forEach(el => {
        switch(el){
          case 0 :
            result.push(0);
            break;
          case 1 :
            result.push(this.conf[0]);
            break;
          case 2 :
            result.push(this.conf[1]);
            break;
          case 3 :
            result.push(this.conf[2]);
            break;
          case 4 :
            result.push(this.conf[3]);
            break;
        } 
      });
      return result;
    },
    validate(){
      //if checked
      if(this.scene==[]){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(e){
      this.valid = true;
      //if i dont know answer -> delete all answers
      if(e.target.value == 0){
        this.scene=[0]
      }else{
        //if previous was idk
        if(this.scene.indexOf(0)!=-1){
          this.scene.shift();
        }
      }
    },
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