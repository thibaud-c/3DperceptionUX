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
  // Results shape answers
  #rootTutoResult
    p.questiontitle.has-text-weight-semibold {{ $t('perc-tut-res-title1') + result + $t('perc-tut-res-title2') }}
    p.paragraph-text.has-text-grey.has-text-justified.b-2(v-html="$t('perc-tut-answers')")
    .columns.column-result-size
      .column.column-center(v-for="img in srcsolution")
          img(:src="'perception/tuto/result_'+img+'.png'")
    p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('perc-tut-resend')")
    #sub-btn.mb-2
      button.button.is-primary(ref="nextB" @click='nextquestion') {{ $t('btn-next') }}
</template>

<script>
import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'ap-tuto-result',
  props:["result"],
  data () {
    return {
      srcsolution:["0","1","2"],
      valid:true
    }
  },
  methods: {
    /**
     * handle the next step process
     */
    nextquestion(){
      this.$emit('nextlod');
      //remove button listerner
      s_methods.remove_entertonext();
    },
  },
  mounted(){
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)
  }
}
</script>

<style>
.column-result-size{
    position:relative;
    width:120%;
    margin: auto;
    left:-10%;
    padding-left: 4px;
}
</style>