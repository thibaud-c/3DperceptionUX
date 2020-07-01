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
  #rootMT
    // ERR Notif
    .notification.errnotif-position.is-danger.is-light(v-if="!valid")
      button.delete(@click="valid=true")
      span {{err_message}}
    // Help notification
    .notification.notif-position(v-if="showtooltip")
      button.delete(@click="showtooltip=false")
      span(v-html="$t('perc-help-3d')")
    // TITLE
    p.sub-question.has-text-weight-semibold(v-if="istosubmit||isquestion" v-html="$t(title)")
    .columns.column-size
      .column
        three.size-threejs(v-if="is3d" :model="'perception/'+path+'/3d.glb'" :view="view" :angles="view_xy" ref="threejs")
      .column.column-center
        // ANSWER DIV
        .b-2.size-leaflet(v-if="istosubmit||isquestion")
          l-map(ref="map" :zoom='l_data["zoom"]' :center='l_data["center"]' :crs="crs")
            l-geo-json(:geojson='geojson' :options-style='styleFunction' @click="selectObject")
        label.checkbox.pl-2(v-if="istosubmit" v-for="ot,id in otherchoices" :class="valid?'valid':'error'")
          input(v-model='other' type='checkbox' :value='id' name='leafletradio' @change="reseterror") 
          |    {{ $t(ot) }}
    #sub-btn.mb-2
        button.button.is-primary(v-if="isquestion" ref="nextB" @click="isquestion=false;is3d=true;") {{ $t("btn-next") }}
        button.button.is-primary(v-if="is3d" ref="nextB" @click="is3d=false;istosubmit=true;saveinputs();title='perc-lod-height-light'") {{ $t("btn-next") }}
        button.button.is-primary(v-if="istosubmit" ref="nextB" @click="nextquestion") {{ $t("btn-valider") }}
        a.pl-2(@click="showtooltip=true") 
          img.image.is-48x48(src="icons/help.png")
</template>

<script>
import three from './mcpt_threejs.vue'
import { CRS } from "leaflet";
import { LMap, LTileLayer, LGeoJson } from 'vue2-leaflet';
import s_methods from '../../../../js/shared_methods.js'

export default {
  name: 'micro-tall-mem',
  props:['path','view','view_xy','footprint','l_data'],
  components: {
    LMap,
    LTileLayer,
    LGeoJson,
    three
  },
  data () {
    return {
      title:'perc-mem-height',
      controls:null,
      crs: CRS.EPSG4326,
      color_unselected:"#606060",
      color_selected:"#fdbe02",
      otherchoices:['perc-lod-height-sameheight'],
      geojson: null,
      building_answered:null,
      click_coordinate:null,
      tries:[],
      userinputs:null,
      first_input_time:null,
      last_input_time:null,
      solution_time:null,
      starting_time:null,
      other:null,
      valid:true,
      showtooltip:false,
      isquestion:true,
      is3d:false,
      istosubmit:false,
      err_message:""
    }
  },
  methods: {
      /**
     * Get answer and send to next
     */
    nextquestion(){
      let ending_time = new Date();
      //validate
      if(!this.validate()){ return; }
      if(this.other!==null){
        this.building_answered=this.other;
        this.click_coordinate =null;
      }
      let data = {
        "res":this.building_answered,
        "time_r":this.solution_time,
        "tries":this.tries,
        "time_s":this.starting_time,
        "time_e":ending_time,
        "inputs":this.userinputs,
        "time_is":this.first_input_time,
        "time_ie":this.last_input_time,
        "click_coordinates":this.click_coordinate
      }
      this.$emit('nextmem',data)
      //remove button listerner
      s_methods.remove_entertonext();

    },
    /**
     * Reset error handler
     */
    reseterror(){
      if(this.other){
        this.tries.push(-9999)
      }
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
    /**
     * Save inputs from threejs
     */
    saveinputs(){
      this.userinputs=this.$refs.threejs.userinputs;
      this.first_input_time=this.$refs.threejs.first_input_time;
      this.last_input_time=this.$refs.threejs.last_input_time;
      // wait next reactivation of $ref
      this.$nextTick(() => {
        this.desactivateControls()
      })
    },
    /**
     * Check if the answer is correct
     */
    validate(){
      //if checked
      if(this.building_answered===null && this.other===null){
        this.err_message=this.$i18n.t('err_no_selection');
        this.valid = false;
        return false;
      }
      return true;
    },
    /**
     * Desactive leaflet map controls
     */
    desactivateControls(){
      //get map object and desactivate controls
      let map = this.$refs.map.mapObject;
      
      map.dragging.disable()
      map.touchZoom.disable();
      map.doubleClickZoom.disable();
      map.scrollWheelZoom.disable();
      map.keyboard.disable();
      map.zoomControl.setPosition('bottomright');

      //map.mapObject.invalidateSize();
    },
    /**
     * Behavior on building click -> select and color it
     */
    selectObject(e){
      this.valid=true;
      //activate selection only for last step
      if(!this.istosubmit){return;}
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
      this.tries.push(this.building_answered);
      this.solution_time = new Date();
    },
  },
  mounted() {
    this.desactivateControls();
    this.starting_time= new Date();
    //add next with enter
    s_methods.entertonext(this.$refs.nextB)
  }, 
  /**
   * Style the map on load
   */
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
  /**
   * Load leaflet map
   */
  async created () {
    const response = await fetch("perception/"+this.footprint+".geojson");
    const data = await response.json();
    this.geojson = data;
  }
}
</script>

<style>

</style>