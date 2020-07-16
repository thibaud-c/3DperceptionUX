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
  // Last Step :)
  #rootThankYou
    p.Maintitle.has-text-weight-semibold {{ $t('perc-tut-res-title1') + result_grade + $t('perc-tut-res-title2') }}
    br
    div(v-if="badgeNB==0")
      img.size-badge(:src="'icons/B0_Pioneer.png'")
      p.paragraph-text.has-text-grey.has-text-centered.has-text-weight-semibold(v-html="$t('perc-tut-res-first')")
    div(v-if="badgeNB==1")
      img.size-badge(:src="'icons/B1_Bull.png'")
      p.paragraph-text.has-text-grey.has-text-centered.has-text-weight-semibold(v-html="$t('perc-tut-res-accuracy1') + this.top_score + $t('perc-tut-res-accuracy2')")
    div(v-if="badgeNB==2")
      img.size-badge(:src="'icons/B2_Ftl.png'")
      p.paragraph-text.has-text-grey.has-text-centered.has-text-weight-semibold(v-html="$t('perc-tut-res-fastest')+ this.top_speed + $t('perc-tut-res-accuracy2')")
    br
    div.divider.divider-size -
    div(v-if="result_grade!=NAN")
      .columns
        .column.column-center
          p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('feed-ty-easiest')")
        .column.column-center
          img.size-diff(:src="'perception/exercices/'+best_scene+'.png'")
      div.divider.divider-size -
      .columns
        .column.column-center
          img.size-diff(:src="'perception/exercices/'+worst_scene+'.png'")
        .column.column-center
          p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('feed-ty-hardest')")
      div.divider.divider-size -
      .columns
        .column.column-center
          p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('feed-ty-questioneasy')")
        .column.column-center
          p.sub-question.has-text-weight-semibold(v-html="$t(questions[best_question])")
      div.divider.divider-size -
      .columns
        .column.column-center
          p.sub-question.has-text-weight-semibold(v-html="$t(questions[worst_question])")
        .column.column-center
          p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('feed-ty-questionhard')")
    br
    div.divider.divider-size -
    br
    p.questiontitle.has-text-weight-semibold {{ $t('feed-ty-thanks') }}
    br
    img.licorne-size.b-2(src="icons/licorne.jpg")
    br
    p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('feed-ty-contact')")
    br
    p.paragraph-text.has-text-grey.has-text-justified.b-2(v-html="$t('end-thanks')")
</template>

<script>
import GConfig from '../../../assets/config.json'
import axios from 'axios';

export default {
  // Last Step :) 
  name: 'fd-thankyou',
  props:["results","id"],
  data () {
    return {
      result_grade:0,
      person:0,
      top_score:null,
      top_speed:null,
      best_scene:0,
      best_question:0,
      worst_scene:1,
      worst_question:1,
      badgeNB:null,
      questions:["perc-lod-leaflet-light","perc-lod-height-light","perc-lod-view","perc-lod-low-light"]
    }
  },
  methods:{
    /**
     * Handle badges drawing
     */
    async buildResultFromScore(scores){
      // Score

      this.result_grade = await scores.data.score;
      this.person = scores.data.nb_user;
      this.top_score = Math.round(scores.data.top_score*100);
      this.top_speed = Math.round(scores.data.top_speed*100);
      // Which badge
      if(this.person<10){
        this.badgeNB=0;
        return;
      }
      if(this.top_score>this.top_speed){
        this.badgeNB=1;
        return;
      }
      this.badgeNB=2;
    },
        /**
     * Check best and worst success rate scene from user answers
     */
    initBestWorstScenes(){
      let t_arr_s = [];
      let f_arr_s = [];
      this.results.forEach(el=>{
        // [true count, false count]
        t_arr_s.push(el.reduce((pre, cur) => (cur) ? ++pre : pre, 0));
        // == false to avoid undefined value with !cur
        f_arr_s.push(el.reduce((pre, cur) => (cur==false) ? ++pre : pre, 0));
      })
      // get index of max
      this.best_scene = t_arr_s.indexOf(Math.max(...t_arr_s));
      this.worst_scene = f_arr_s.indexOf(Math.max(...f_arr_s));
    },
    /**
     * Check best and worst success rate question from user answers
     */
    initBestWorstQuestions(){
      // inverse line column were max -> id 2
      let tsp_array = this.results[2].map((_, colIndex) => this.results.map(row => row[colIndex]));
      let t_arr_q = [];
      let f_arr_q = [];
      tsp_array.forEach(el=>{
        // [true count, false count]
        t_arr_q.push(el.reduce((pre, cur) => (cur) ? ++pre : pre, 0));
        // == false to avoid undefined value with !cur
        f_arr_q.push(el.reduce((pre, cur) => (cur==false) ? ++pre : pre, 0));
      });
      // get index of max
      this.best_question = t_arr_q.indexOf(Math.max(...t_arr_q));
      this.worst_question = f_arr_q.indexOf(Math.max(...f_arr_q));
    },
    /**
     * Get scores from db
     */
    async getScoresFromDB(){
      // Get config from back end
      let path = GConfig.URL_BACKEND + GConfig.URL_POSTDATA + this.id + "/scores";
      try{
        //Request
        let response = await axios.get(path);
        return await response.data;        
      }catch(err) {
        console.log(err);     
      }
    }
  },
  async mounted(){
    /** Get best/worst scenes **/
    this.initBestWorstScenes()

    /** Get best/worst question **/
    this.initBestWorstQuestions()

    /** Get data from db **/
    this.buildResultFromScore(await this.getScoresFromDB());
         
    // Send end time to db 
    await this.send("end_at",new Date())
  }    
}
</script>

<style>
.licorne-size{
  width:50%;
}
.size-diff{
  width:80%;
}
.size-badge{
  width:30%;
}
.divider-size{
  width:50%;
  margin:auto !important;
  padding-bottom:3%;
}
</style>