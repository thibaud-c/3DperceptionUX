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
    p.questiontitle.has-text-weight-semibold {{ $t('perc-tut-res-title1') + result_grade + $t('perc-tut-res-title2') }}
    br
    div(v-if="result_grade!=100 && result_grade!=0")
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
    p.paragraph-text.has-text-grey.has-text-justified.b-2(v-html="$t('feed-ty-contact')")
</template>

<script>
export default {
  // Last Step :) 
  name: 'fd-thankyou',
  props:["results"],
  data () {
    return {
      result_grade:0,
      best_scene:0,
      best_question:0,
      worst_scene:1,
      worst_question:1,
      questions:["perc-lod-leaflet-light","perc-lod-height-light","perc-lod-view","perc-lod-low-light"]
    }
  },
  mounted(){

    /** Grade **/

    let flatten_result = this.results.flat();
    // nb of occurence true / by total false, true
    this.result_grade = Math.round(flatten_result.reduce((pre, cur) => (cur) ? ++pre : pre, 0) / flatten_result.length *100);
    
    /** Get best/worst scenes **/

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

    /** Get best/worst question **/

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
.divider-size{
  width:50%;
  margin:auto !important;
  padding-bottom:3%;
}
</style>