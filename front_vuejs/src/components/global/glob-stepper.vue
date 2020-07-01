<!--
MIT License

Copyright (c) [2018] [Thibaud Chassin]

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
  #root.stepper
    ul.steps.is-thin.is-centered.has-content-centered
      li.steps-segment.has-gaps(:class="steps==0?'is-active':''")
        span.steps-marker
        .steps-content
          p.heading {{ $t('main-Introduction') }}
      li.steps-segment.has-gaps(:class="steps==1?'is-active':''")
        span.steps-marker
        .steps-content
          p.heading {{ $t('main-socio') }}
      li.steps-segment.has-gaps(:class="steps==2?'is-active':''")
        span.steps-marker
        .steps-content
          p.heading {{ $t('main-perception') }}
      li.steps-segment.has-gaps(:class="steps==3?'is-active':''")
        span.steps-marker
        .steps-content
          p.heading {{ $t('main-commentaire') }}
</template>

<script>
export default {
  name: 'stepper',
  props: {
    steps:Number
  },
}
</script>

<style>
.stepper{
  margin:auto;
  margin-top:2%;
  width:90%;
  top:6%;
  position: relative;
}
</style>