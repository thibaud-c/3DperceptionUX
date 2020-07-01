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
  #rootSD_W
    // modal age
    .modal(:class="ismodalage?'is-active':''")
      .modal-background
      .modal-card
        header.modal-card-head
          p.modal-card-title {{ user_name + $t('verif-age-title') }}
        section.modal-card-body {{ $t('verif-age-content') }}
        footer.modal-card-foot
          button.button.is-success(@click='ismodalage=false') {{ $t('verif-age-valid') }}
          button.button(@click='ismodalage=false; reload();') {{ $t('verif-age-cancel') }}
    // ERR Notif
    .notification.errnotif-position.is-danger.is-light(v-if="!valid")
      button.delete(@click="valid=true")
      span {{err_message}}
    // TITLE
    p.questiontitle.has-text-weight-semibold {{ user_name + $t('socio-in-title') }}
    .field.is-grouped.is-grouped-multiline
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_1")
        p(v-html="$t(p_text)")
      .paragraph-text.has-text-grey.has-text-justified(v-html="user_name")
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_2")
        p(v-html="$t(p_text)")
      // date
      .select.p-2.b-2(:class="isvaliddate?'valid':'is-danger'" @change='resetdateerror()')
        select(v-model="selected_date")
          option.selected(v-for="d in date")
            p {{d}} 
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_3")
        p(v-html="$t(p_text)")
      // country grew
      .select.p-2.b-2
        select(v-model="selected_country_gre" @change='updatedvalue()')
          option.selected(v-for="i in $t('countries').length")
            p {{$t('countries')[i-1]}} 
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_4")
        p(v-html="$t(p_text)")
      // density grew
      .select.p-2.b-2
        select(v-model="selected_density_gre")
          option.selected(v-for="d,index in density" :value="index")
            p {{$t(d)}} 
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_5")
        p(v-html="$t(p_text)")
      // education
      .select.p-2.b-2
        select(v-model="selected_education")
          option.selected(v-for="i,index in education" :value="index")
            p {{$t(i)}} 
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_6")
        p(v-html="$t(p_text)")
      // country 
      .select.p-2.b-2(:class="isvalidcountry?'valid':'is-danger'" @change="resetcountryerror()")
        select(v-model="selected_country_cur")
          option.selected(v-for="i in $t('countries').length")
            p {{$t('countries')[i-1]}} 
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_7")
        p(v-html="$t(p_text)")
      // density
      .select.p-2.b-2
        select(v-model="selected_density_cur")
          option.selected(v-for="d,index in density" :value="index")
            p {{$t(d)}} 
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_5bis")
        p(v-html="$t(p_text)")
    .field.is-grouped.is-grouped-multiline
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_8")
        p(v-html="$t(p_text)")
      //gender
      .select.p-2.b-2(:class="isvalidgender?'valid':'is-danger'" @change="resetgendererror()")
        select(v-model="selected_gender")
          option.selected(v-for="d,index in gender" :value="index")
            p {{$t(d)}} 
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_9")
        p(v-html="$t(p_text)")
      //technophile
      .select.p-2.b-2
        select(v-model="selected_tech")
          option.selected(v-for="d,index in techno" :value="index")
            p {{$t(d)}} 
      .paragraph-text.has-text-grey.has-text-justified(v-for="p_text in parag_10")
        p(v-html="$t(p_text)")  
    #sub-btn.mb-2
      button.button.is-primary.mb-2(ref="nextB" @click='addStep') {{ $t('btn-valider') }}
</template>

<script>
import s_methods from '../../../js/shared_methods.js'

export default {
  name: 'id-welcome',
  selected_date:"",
  props:['user_name'],
  data () {
    return {
      parag_1:["socio-in-t1a","socio-in-t1b","socio-in-t1c","socio-in-t1d","socio-in-t1e","socio-in-t1f"],
      parag_2:["socio-in-t2a","socio-in-t2b","socio-in-t2c","socio-in-t2d"],
      parag_3:["socio-in-t3a","socio-in-t3b","socio-in-t3c","socio-in-t3d","socio-in-t3e","socio-in-t3f","socio-in-t3g"],
      parag_4:["socio-in-t4a","socio-in-t4b","socio-in-t4c","socio-in-t4d","socio-in-t4e","socio-in-t4f","socio-in-t4g","socio-in-t4h","socio-in-t4i","socio-in-t4j"],
      parag_5:["socio-in-t5a","socio-in-t5b","socio-in-t5c","socio-in-t5d","socio-in-t5e","socio-in-t5f","socio-in-t5g"],
      parag_6:["socio-in-t6a","socio-in-t6b","socio-in-t6c","socio-in-t6d"],
      parag_7:["socio-in-t7a","socio-in-t7b","socio-in-t7c"],
      parag_5bis:["socio-in-t5a"],
      parag_8:["socio-in-t8a","socio-in-t8b","socio-in-t8c","socio-in-t8d","socio-in-t8e","socio-in-t8f","socio-in-t8g","socio-in-t8h","socio-in-t8i"],
      parag_9:["socio-in-t9a","socio-in-t9b","socio-in-t9c"],
      parag_10:["socio-in-t10a","socio-in-t10b","socio-in-t10c","socio-in-t10d","socio-in-t10e","socio-in-t10f","socio-in-t10g","socio-in-t10h","socio-in-t10i","socio-in-t10j","socio-in-t10k","socio-in-t10l","socio-in-t10m","socio-in-t10n","socio-in-t10o"],
      selected_date:null,
      date:["2020","2019","2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981","1980","1979","1978","1977","1976","1975","1974","1973","1972","1971","1970","1969","1968","1967","1966","1965","1964","1963","1962","1961","1960","1959","1958","1957","1956","1955","1954","1953","1952","1951","1950","1949","1948","1947","1946","1945","1944","1943","1942","1941","1940","1939","1938","1937","1936","1935","1934","1933","1932","1931","1930","1929","1928","1927","1926","1925","1924","1923","1922","1921","1920"],
      selected_density_cur:null,
      selected_country_cur:null,
      density:["socio-in-dense--","socio-in-dense-","socio-in-dense=","socio-in-dense+","socio-in-dense++"],
      selected_country_gre:null,
      selected_density_gre:null,
      education:["socio-in-obligatoire","socio-in-secondaire-prof","socio-in-secondaire-général","socio-in-sup-prof","socio-in-sup-uni","socio-in-autre"],
      selected_education:null,
      selected_gender:null,
      gender:["socio-in-masc","socio-in-femi"],
      selected_tech:null,
      techno:["socio-in-tech--", "socio-in-tech-", "socio-in-tech=","socio-in-tech+","socio-in-tech++"],
      isvalidgender:true,
      isvalidcountry:true,
      isvaliddate:true,
      ismodalage:false,
      valid:true,
    } 
  },
  methods: {
    addStep(){
      if(!this.validate()){ return; }
      let json_answer = this.create_json()
      //save and pass next question
      this.$emit('nextsociostep',json_answer);
    },
    /**
     * Concat json value
     */
    create_json(){
      let json = {};
      //age
      if (this.selected_date!=null){
        let year = new Date().getFullYear();
        json["age"] = year-this.selected_date;
      }

      //genre
      if (this.selected_gender!=null){
        json["gender"] = this.selected_gender;
      }

      //education
      if (this.selected_education!=null){
        json["education"] = this.selected_education;
      }

      //living currently
      if (this.selected_country_cur!=null){
        json["location_country"] = this.selected_country_cur;
      }
      if (this.selected_density_cur!=null){
        json["location_density"] = this.selected_density_cur;
      }

      //grew
      if (this.selected_country_gre!=null){
        json["grew_country"] = this.selected_country_gre;
      }
      if (this.selected_density_gre!=null){
        json["grew_density"] = this.selected_density_gre;
      }

      //tech
      if (this.selected_tech!=null){
        json["frequency_3d"] = this.selected_tech;
      }
      return json
    },
    /**
     * Validation process : Gender / age / Country are required
     */
    validate(){
      //check date
      if(this.selected_date==null){
        this.isvaliddate=false;
      }
      //check country
      if(this.selected_country_cur==null){
        this.isvalidcountry=false;
      }
      //check gender
      if(this.selected_gender==null){
        this.isvalidgender=false;
      }
      // Create error
      if(!(this.isvalidgender&&this.isvaliddate&&this.isvalidcountry)){
        this.valid=false;
        this.err_message=this.$i18n.t('err_empty_field_select');
        return false;
      }
      return true;
    },
    /**
     * Reset Date error
     */
    resetdateerror(){
      this.isvaliddate=true;
      this.valid=true;
      //create mode check age
      if(new Date().getFullYear() - this.selected_date < 18){
        this.ismodalage=true;
      }
    },
    /**
     * Reset gender error
     */
    resetgendererror(){
      this.isvalidgender=true;
      this.valid=true;
    },
    /**
     * Reset country error
     */
    resetcountryerror(){
      this.isvalidcountry=true;
      this.valid=true;
    },
    /**
     * Automate fill of current country according to the grew country
     */
    updatedvalue(){
      if(this.selected_country_cur==null){
        this.selected_country_cur = this.selected_country_gre;
        this.isvalidcountry=true;
      }
    },
    reload(){
      location.reload();
    }
  },
  mounted(){
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)
  }
}
</script>

<style>
.p-2{
  padding-left:0.5%;
  padding-right:0.5%;
  position: relative;
}
</style>