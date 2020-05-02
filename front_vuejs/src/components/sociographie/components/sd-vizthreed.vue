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
  #rootVizthreeD
    //viz3d 
    p.questiontitle.has-text-weight-semibold {{ $t('socio-vd-question') }}
    #sub-dalt    
      label.radio.pl-2(v-for="img,id in srcsolution" :class="valid?'valid':'error'")
        input(v-model='solution' type='radio' :value='img' name='3dradio' @change="reseterror") 
        img.image-sol-size(:src="img")
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'sd-vizthreed',
  data () {
    return {
      srcplan2D:'tests/plan2D.png',
      srcsolution:[],
      solution:"",
      valid:true
    }
  },
  methods: {
    nextquestion(){
      // aimed answer -> 2
      if(!this.validate()){ return; }
      let id_sol = this.solution.split("/")[1][0];
      if(id_sol==this.srcsolution.length){ id_sol = -1; }
      let json_answer = {"exercice_3d":id_sol}
      this.$emit('nextsociostep',json_answer);
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
    //Fisher-Yates algorithm
    shuffle(array) {
      var currentIndex = array.length, temporaryValue, randomIndex;

      // While there remain elements to shuffle...
      while (0 !== currentIndex) {

        // Pick a remaining element...
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;

        // And swap it with the current element.
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
      }
      return array;
    }
  }, mounted () {
    // random shown solution
    let randomized_answers = [0,1,2,3,4];
    randomized_answers = this.shuffle(randomized_answers);
    randomized_answers.forEach(sol => {
      this.srcsolution.push("tests/"+sol+".png");
    });
    //add i don't know 
    this.srcsolution.push("tests/5.png");
  }
}
</script>

<style>
.image-sol-size{
    height:125px;
    width:150px;
    margin:auto;
}
</style>