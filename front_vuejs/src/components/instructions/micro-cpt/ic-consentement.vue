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
  #rootIC_C
    p.questiontitle.has-text-weight-semibold {{ $t('intro-cc-concentement') }}
    //text rules loop
    #rules(v-for="rule in consent_rules")
      p.paragraph-text.has-text-grey.has-text-justified •  {{ $t(rule) }}
      br
    br
    //consent
    label.checkbox.has-text-weight-semibold(:class="valid?'valid':'error'")
      input(v-model="consent" name="conscheck" type='checkbox' @change="reseterror") 
      |     {{ $t("intro-cc-declaration") }}
    .sub-btns.mb-2
      button.button.is-primary.mb-2(@click='addStep') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'ic-consentment',
  data () {
    return {
      consent:false,
      consent_rules:['intro-cc-volontariat','intro-cc-anonymat','intro-cc-film'],
      valid:true
    }
  },
  methods: {
    addStep(){
      //validate
      if(!this.validate()){ return; }
      this.$emit('nextintrostep');
    },
    validate(){
      //checked
      if(!this.consent){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    }
  }
}
</script>

<style>
</style>