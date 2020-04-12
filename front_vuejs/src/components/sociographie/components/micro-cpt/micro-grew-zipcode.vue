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
  #rootMGR_Z
    #sub-cp(v-if="npa_cp != 2")
      p.sub-question.has-text-weight-semibold.has-text-centered ★ 
      p.sub-question.has-text-weight-semibold {{ npa_cp==0?$t('socio-gr-questionCP'):$t('socio-gr-questionNPA') }}
      .control.cpt-40.b-2(v-if="!refus && npa_cp != 2")
        input.input( type='text' v-model='codepost' :placeholder="npa_cp==0?'00000':'0000'" :class="valid?'':'is-danger'" @change="reseterror")
    // country
    #sub-co(v-if="npa_cp == 2")
      p.sub-question.has-text-weight-semibold.has-text-centered ★ 
      p.sub-question.has-text-weight-semibold {{ $t('socio-gr-questionOth') }}
      .select.b-2(v-if="!refus && npa_cp == 2" :class="valid?'':'is-danger'")
        select(v-model="country" @change="reseterror")
          option.selected(v-for="co in countries" :key="co")
            p {{co}} 
    //refus
    label.checkbox.pl-2
      input(v-model="refus" name="grzcheck" type='checkbox' @change="isrefus(),reseterror()") 
      |   {{ $t("reponse-refus") }}
    //button
    #sub-btn.mb-2
      //button.button.is-text(@click='') {{ $t('btn-previous') }}
      button.button.is-primary(@click='nextquestion') {{ $t('btn-valider') }}
</template>

<script>
export default {
  name: 'micro-gr-zip',
  props: {
    npa_cp:Number
  },
  data () {
    return {
      codepost:null,
      country:null,
      countries:['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua & Deps', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Rep', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Congo (Democratic Rep)', 'Costa Rica', 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland (Republic)', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North', 'Korea South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Burma', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'St Kitts & Nevis', 'St Lucia', 'Saint Vincent & the Grenadines', 'Samoa', 'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'],
      valid:true,
      refus:false
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      // initiate context (cp or country) and return value
      let value_cp = this.codepost;
      let context = 0;
      if(this.refus){
        value_cp = -0;
        context = 2;
      }
      if(this.country!=null){
        value_cp = this.country;
        context = 1;
      }
      // context 0 -> cp / 1 -> country / 2 -> refusal
      //save and pass next question
      this.$emit('nextgrew',[value_cp,context]);
    },
    validate(){
      let er = /^-?[0-9]+$/;
      if(this.refus){return true;}
      if(this.country!=null){return true;}
      //number and country/filling
      if((this.codepost === null || this.codepost==='' || !er.test(this.codepost)) && this.country === null){
        this.valid = false;
        return false;
      }
      // NPA number and CP number
      if(this.codepost.length != 5 && this.npa_cp == 0 || this.codepost.length != 4 && this.npa_cp == 1){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    },
    isrefus(){
      this.codepost=null;
      this.country=null;
    },
  }
}
</script>

<style>
</style>