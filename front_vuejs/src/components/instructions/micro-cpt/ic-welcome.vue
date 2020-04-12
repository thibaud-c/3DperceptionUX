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
  #rootWelcome
    p.questiontitle.has-text-weight-semibold {{ $t('intro-we-bonjour') }}
    p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('intro-we-bienvenue')")
    p.paragraph-text.has-text-grey.has-text-justified {{ $t('intro-we-etude') }}
    p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('intro-we-aide')")
    br
    p.paragraph-text.has-text-grey.has-text-justified {{ $t('intro-we-remerciements') }}
    p.paragraph-text.has-text-grey.has-text-justified(v-html="$t('intro-we-contact')")
    .sub-btns.mb-2
      button.button.is-primary.mb-2(@click='addStep') {{ $t('btn-start') }}
</template>

<script>
export default {
  name: 'ic-welcome',
  methods: {
    addStep(){
      //save and pass next step
      this.$emit('nextintrostep');
    }
  }
}
</script>

<style>
</style>