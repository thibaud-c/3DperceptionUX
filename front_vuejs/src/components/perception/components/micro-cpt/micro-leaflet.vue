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
  #leafletcontainer
    p.sub-question.has-text-weight-semibold.has-text-centered ★ 
    p.sub-question.has-text-weight-semibold(v-html="$t('perc-lod-height')")
    .b-2.size-leaflet
      l-map(ref="map" :zoom='zoom' :center='center' :crs="crs")
        l-geo-json(:geojson='geojson' :options-style='styleFunction' @click="selectObject")
    label.radio.pl-2(v-for="ot,id in otherchoices" :class="valid?'valid':'error'")
      input(v-model='other' type='radio' :value='id' name='leafletradio' @change="reseterror") 
      |    {{ $t(ot) }}
    #sub-btn.mb-2
      //button.button.is-text(@click="") {{ $t("btn-previous") }}
      button.button.is-primary(@click="nextquestion") {{ $t("btn-valider") }}
</template>
<script>
import { CRS } from "leaflet";
import { LMap, LTileLayer, LGeoJson } from 'vue2-leaflet';
  
export default {
  
  name: 'micro-leaflet',
  components: {
    LMap,
    LTileLayer,
    LGeoJson
  },
  props:['footprint','center','zoom'],
  data () {
    return {
      crs: CRS.EPSG4326,
      otherchoices:['reponse-no-answer','perc-lod-height-sameheight'],
      geojson: null,
      building_answered:null,
      click_coordinate:null,
      other:null,
      valid:true,
      color_unselected:"#606060",
      color_selected:"#fdbe02"
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      if(this.other!==null){
        this.building_answered=this.other;
        this.click_coordinate =null;
      }
      this.$emit('nextlod',[this.building_answered,this.click_coordinate])
    },
    validate(){
      //if checked
      if(this.building_answered===null && this.other===null){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid=true;
      //Desactivate selections
      this.color_selected="#606060"
      // look for building selected and style it in grey
      this.$refs.map.mapObject.eachLayer(layer =>{
        //every layer stylable
        if(typeof layer.feature!=='undefined'){
          //selected building
          if(layer.feature.properties.osm_id == this.building_answered){
            layer.setStyle({fillColor:this.color_selected})
          }
        }
      })
      //reactivate selection
      this.color_selected="#fdbe02"
      this.building_answered = null;
      this.click_coordinate = null;
    },
    desactivateControls(){
      //get map object and desactivate controls
      let map = this.$refs.map.mapObject;  
      map.dragging.disable()
      map.touchZoom.disable();
      map.doubleClickZoom.disable();
      map.scrollWheelZoom.disable();
      map.keyboard.disable();
      map.zoomControl.remove();

      //map.mapObject.invalidateSize();
    },
    selectObject(e){
      //update the answer 
      this.building_answered = e.layer.feature.properties.osm_id;
      this.click_coordinate = e.latlng;
      this.other = null;
      e.target.eachLayer(layer => {
          layer.setStyle({
            opacity: 1,
            fillColor: this.color_unselected,
            fillOpacity: 1
        });
      })
      e.layer.setStyle({
        opacity:1,
        fillColor:this.color_selected,
        fillOpacity: 1
      });
    },
  },
  computed: {
    styleFunction() {
      const fillColor = this.fillColor; // important! need touch fillColor in computed for re-calculate when change fillColor
      return () => {
        return {
          opacity: 1,
          color:this.color_unselected,
          fillColor:fillColor,
          weight: 0,
          fillOpacity: 1
        };
      };
    },
  },
  mounted() {
    this.desactivateControls()
  },
  async created () {
    const response = await fetch(this.footprint);
    const data = await response.json();
    this.geojson = data;
  }
}
</script>

<style>
</style>