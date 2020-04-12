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
  #rootDP
    //Participation
    part(v-if="pa_step==0" @nextparticipation="nextquestion")
    part_3d(v-if="pa_step==1" @nextparticipation="nextquestion")
    part_ro(v-if="pa_step==2" @nextparticipation="nextquestion")
    part_ro_o(v-if="pa_step==3" @nextparticipation="nextquestion")
    //part_th(v-if="pa_step==4" @nextparticipation="nextquestion")
    //part_th_o(v-if="pa_step==5" @nextparticipation="nextquestion")
    part_nu(v-if="pa_step==4" @nextparticipation="nextquestion")
</template>

<script>
  import part from './micro-cpt/micro-participation.vue'
  import part_3d from './micro-cpt/micro-participation-3d.vue'
  import part_ro from './micro-cpt/micro-participation-role.vue'
  import part_ro_o from './micro-cpt/micro-participation-role-other.vue'
  import part_th from './micro-cpt/micro-participation-theme.vue'
  import part_th_o from './micro-cpt/micro-participation-theme-other.vue'
  import part_nu from './micro-cpt/micro-participation-number.vue'
export default {
  name: 'sd-participation',
    components : { 
      part,
      part_3d,
      part_ro,
      part_ro_o,
      part_th,
      part_th_o,
      part_nu
    },
  data () {
    return {
        pa_step:0,
        json_answer:{}
    }
  },
  methods: {
    nextquestion(data){
      // save Threed and add step if needed
      if(this.pa_step==0){
        this.json_answer["participation"] = data[0];
        //next step needed?
        if(data[1]){
          this.pa_step++;
          return;
        }
      }
      if(this.pa_step==1){
        this.json_answer["participation_3d"] = data;
        //next step needed?
        this.pa_step++;
        return;
      }
      if(this.pa_step==2){
        this.json_answer["participation_role"] = data[0];
        //next step needed?
        if(data[1]){
          this.pa_step++;
          return;
        }
        this.pa_step+=2;
        return;
      }
      if(this.pa_step==3){
        this.json_answer["participation_role_other"] = data;
        //next step needed?
        this.pa_step++;
        return;
      }
      if(this.pa_step==4){
        this.json_answer["participation_number"] = data;
      }
      //save and pass next question
      this.$emit('nextsociostep',this.json_answer);
    },
  }
}
</script>

<style>
</style>