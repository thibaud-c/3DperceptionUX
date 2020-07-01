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
  #rootMT
    // ERR Notif
    .notification.errnotif-position.is-danger.is-light(v-if="!valid")
      button.delete(@click="valid=true")
      span {{err_message}}
    // Help notification
    .notification.notif-position(v-if="showtooltip")
      button.delete(@click="showtooltip=false")
      span(v-html="$t('perc-help-3d')")
    // TITLE
    p.sub-question.has-text-weight-semibold(v-html="$t('perc-lod-view')")
    .columns.column-size
      .column
        three.size-threejs(:model="'perception/'+path+'/3d_view.glb'" :view="view" :angles="view_xy" ref="threejs")
      .column.column-center
        // ANSWER DIV
        label.radio.pl-2(v-for="sol,id in views_solutions" :class="valid?'valid':'error'")
          input(v-model='solution' type='radio' :value='id' name='viewradio' @change="reseterror" @click="$event.target.blur()") 
          |    {{ $t(sol) }}
    #sub-btn.mb-2
        button.button.is-primary(ref="nextB" @click="nextquestion") {{ $t("btn-valider") }}
        a.pl-2(@click="showtooltip=true") 
          img.image.is-48x48(src="icons/help.png")
</template>

<script>
import three from './mcpt_threejs.vue'

import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'micro-view',
  props:['path','view','view_xy'],
  components : { 
    three
  },
  data () {
    return {
      solution:null,
      tries:[],
      solution_time:null,
      starting_time:null,      
      views_solutions:["perc-lod-view0","perc-lod-view1","perc-lod-view1b","perc-lod-view2"],
      showtooltip:false,
      valid:true,
      err_message:""
    }
  },
  methods: {
      /**
     * Format answer and send to next
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
        "inputs":this.$refs.threejs.userinputs,
        "time_is":this.$refs.threejs.first_input_time,
        "time_ie":this.$refs.threejs.last_input_time,
      }
      this.$emit('nextlod',data)
      //remove button listerner
      s_methods.remove_entertonext()
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
     * Check validation
     */
    validate(){
      //if checked
      if(this.solution===null){
        this.err_message=this.$i18n.t('err_no_selection');
        this.valid = false;
        return false;
      }
      return true;
    }
  },
  mounted() {
    this.starting_time= new Date();
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)

  }
}
</script>

<style>
</style>