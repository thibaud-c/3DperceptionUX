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
  #rootMIMGMAP
    // ERR Notif
    .notification.errnotif-position.is-danger.is-light(v-if="!valid")
      button.delete(@click="valid=true")
      span {{err_message}}
    // Help notification
    .notification.notif-position(v-if="showtooltip")
      button.delete(@click="showtooltip=false")
      span(v-html="$t('perc-help-3d')")
    // TITLE
    p.sub-question.has-text-weight-semibold(v-if="istosubmit||isquestion" v-html="$t(title)")
    .columns.column-size
      .column   
        three.size-threejs(v-if="is3d" :model="'perception/'+path+'/3d.glb'" :view="view" :angles="view_xy" ref="threejs")
      .column.column-center
          // ANSWER DIV
          label.radio.size-whichleafletmap(v-if="istosubmit || isquestion" v-for="img in answer" :class="valid?'valid':'error'")
            .level          
              input(v-if="istosubmit" v-model='solution' ref="map_choice" type='radio' :value='img' name='imgmap' @change="reseterror" @click="$event.target.blur()") 
              img.b-2(:src="'perception/'+path+'/'+img+'.png'")
    #sub-btn.mb-2
        button.button.is-primary(v-if="isquestion" ref="nextB" @click="isquestion=false;is3d=true;") {{ $t("btn-next") }}
        button.button.is-primary(v-if="is3d" ref="nextB" @click="saveinputs();is3d=false;istosubmit=true;title='perc-mem-map2'") {{ $t("btn-next") }}
        button.button.is-primary(v-if="istosubmit" ref="nextB" @click="nextquestion") {{ $t("btn-valider") }}
        a.pl-2(@click="showtooltip=true") 
          img.image.is-48x48(src="icons/help.png")
</template>

<script>
import three from './mcpt_threejs.vue'
import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'lod-micro-ima-map',
  props:['path','view','answer','view_xy'],
  components : { 
    three
  },
  data () {
    return {
      title:'perc-mem-map',
      solution:null,
      tries:[],
      valid:true,
      userinputs:null,
      first_input_time:null,
      last_input_time:null,
      solution_time:null,
      starting_time:null,
      showtooltip:false,
      isquestion:true,
      is3d:false,
      istosubmit:false,
      err_message:""   
    }
  },
  methods: {
      /**
     * Get answer and send to next
     */
    nextquestion(){
      let ending_time = new Date();
      //validate
      if(!this.validate()){ return; }
      let data = {
        "res":this.solution,
        "time_r":this.solution_time,
        "tries":this.tries,
        "time_s":this.starting_time,
        "time_e":ending_time,
        "inputs":this.userinputs,
        "time_is":this.first_input_time,
        "time_ie":this.last_input_time,
      }
     this.$emit('nextmem',data)
     //remove button listerner
     s_methods.remove_entertonext();
    },
    /**
     * Save inputs from threejs
     */
    saveinputs(){
      this.userinputs=this.$refs.threejs.userinputs;
      this.first_input_time=this.$refs.threejs.first_input_time;
      this.last_input_time=this.$refs.threejs.last_input_time;
    },
    /**
     * Reset error handler
     */
    reseterror(){
        this.valid = true;
        this.tries.push(this.solution);
        this.solution_time = new Date();
    },
    /**
     * Check if the answer is correct
     */
    validate(){
      //if checked
      if(this.solution===null){
        this.valid = false;
        this.err_message=this.$i18n.t('err_no_selection');
        return false;
      }
      return true;
    }
  },
  mounted(){
    this.starting_time= new Date();
    //add next with enter
    s_methods.entertonext(this.$refs.nextB);
  }
}
</script>

<style>
</style>