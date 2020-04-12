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
  #rootAge
    //question
    p.questiontitle.has-text-weight-semibold {{ $t("socio-ag-question") }}
    //select age
    .select.b-2(v-if="!refus" :class="valid?'valid':'is-danger'")
      select(v-model="selected_date" @change="reseterror")
        //age loop
        option.selected(v-for="d in date")
          p {{d}} 
    br
    //refus
    label.checkbox.pl-2
      input(v-model="refus" name="agecheck" type='checkbox' @change="isrefus(),reseterror()") 
      |   {{ $t("reponse-refus") }}
    #sub-btn.mb-2
      //button.button.is-text(@click="") {{ $t("btn-previous") }}
      button.button.is-primary(@click="nextquestion") {{ $t("btn-valider") }}
</template>

<script>
export default {
  name: "sd-age",
  data () {
    return {
      //date default
      selected_date:null,
      //possible age 
      date:["2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981","1980","1979","1978","1977","1976","1975","1974","1973","1972","1971","1970","1969","1968","1967","1966","1965","1964","1963","1962","1961","1960","1959","1958","1957","1956","1955","1954","1953","1952","1951","1950","1949","1948","1947","1946","1945","1944","1943","1942","1941","1940","1939","1938","1937","1936","1935","1934","1933","1932","1931","1930","1929","1928","1927","1926","1925","1924","1923","1922","1921","1920"],
      refus:false,
      valid:true
    }
  },
  methods: {
    //create json answer and send
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      if (this.refus){
        this.selected_date=0
      }
      //calculate age
      let year = new Date().getFullYear();
      let json_answer = {"age": year-this.selected_date};
      //save and pass next question
      this.$emit("nextsociostep",json_answer);
    },
    validate(){
      // check answer exist
      if(this.selected_date===null && !this.refus){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid = true;
    },
    isrefus(){
      this.selected_date=null;
    },
  }
}
</script>
 
<style>
</style>