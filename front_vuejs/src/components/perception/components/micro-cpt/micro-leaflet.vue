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
    p.sub-question.has-text-weight-semibold {{ $t('perc-lod-height') }}
    .size-leaflet.b-2
      l-map(ref="map" :zoom='zoom' :center='center')
        l-geo-json(:geojson='geojson' :options-style='styleFunction' @click="selectObject")
    label.checkbox.pl-2(:class="valid?'valid':'error'")
      input(v-model='noAnswer' type='checkbox' :value='-0' name='3dradio' @change="reseterror") 
      |   {{ $t('reponse-no-answer') }}
    #sub-btn.mb-2
      //button.button.is-text(@click="") {{ $t("btn-previous") }}
      button.button.is-primary(@click="nextquestion") {{ $t("btn-valider") }}
</template>
<script>
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
      geojson: null,
      building_answered:null,
      noAnswer:false,
      valid:true,
      color_unselected:"#606060",
      color_selected:"#fdbe02"
    }
  },
  methods: {
    nextquestion(){
      //validate
      if(!this.validate()){ return; }
      if(this.noAnswer){this.building_answered=-0}
      this.$emit('nextlod',this.building_answered)
    },
    validate(){
      //if checked
      if(this.building_answered===null && this.noAnswer==false){
        this.valid = false;
        return false;
      }
      return true;
    },
    reseterror(){
      this.valid=true;
      //lock selections
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
      if(!this.noAnswer){this.color_selected="#fdbe02"}
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
.size-leaflet{
  height:450px;
  width:450px;
  margin:auto;
}
.leaflet-container {
    background-color:rgba(255,0,0,0.0);
}
</style>