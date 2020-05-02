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
  #ThreejsModel
    p.questiontitle.has-text-weight-semibold {{ $t('perc-lod-3dscene') }}
    p.paragraph-text.has-text-grey.has-text-justified.b-2(v-if="model==='perception/tuto/3d.glb'" v-html="$t('perc-tut-3d')")
    .level
      img.size-tuto-img(:src="src_img_pitch")
      #threecontainer.size-threejs
      img.size-tuto-img(:src="src_img_yaw")
    #sub-btn.mb-2
      //button.button.is-text(@click="") {{ $t("btn-previous") }}
      button.button.is-primary(@click="nextquestion") {{ $t("btn-valider") }}
</template>
<script>
import * as THREE from  'three/build/three.js'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';

//import { MTLLoader } from "three/examples/jsm/loaders/MTLLoader.js";
  
export default {
  name: 'micro-three',
  props:['model', "view"],
  data () {
    return {
      camera: null,
      userinputs: [],
      scene: null,
      renderer: null,
      mesh: null,
      controls:null,
      width_container:450,
      height_container:450,
      src_img_pitch:"icons/pitch.png",
      src_img_yaw:"icons/yaw.png"
    }
  },
  methods: {
    nextquestion(){
      this.$emit('nextlod',this.userinputs)
    },
    update(){
      document.addEventListener( 'keydown', (e)=>{
        switch (e.keyCode) {
          case 37:
            this.mesh.rotation.y -= 0.1;
          break;
          case 38:

            this.mesh.rotation.x -= 0.1;
            if(this.mesh.rotation.x < 0){this.mesh.rotation.x = 0}
          break;
          case 39:
            this.mesh.rotation.y += 0.1;
          break;
          case 40:
            this.mesh.rotation.x += 0.1;
            if(this.mesh.rotation.x > 0.78){this.mesh.rotation.x = 0.78}
          break;
        }   
      });
    },
    init() {
      let container = document.getElementById('threecontainer');

      this.scene = new THREE.Scene();
      this.camera = new THREE.PerspectiveCamera(70, this.height_container/this.width_container, 0.01, 1200);
      this.camera.position.x = this.view["x"];
      this.camera.position.y = this.view["y"];
      this.camera.position.z = this.view["z"];
      this.scene.add(this.camera)

      this.renderer = new THREE.WebGLRenderer({antialias: true});
      this.renderer.setSize(this.height_container, this.width_container);
      container.appendChild(this.renderer.domElement);

      this.renderer.gammaOutput = true;
      this.renderer.gammaFactor = 2.2; 
      this.renderer.physicallyCorrectLights=true;

      let materialArray = [];
      let texture_ft = new THREE.TextureLoader().load('perception/textures/sky.png');
      let texture_bk = new THREE.TextureLoader().load('perception/textures/sky.png');
      let texture_up = new THREE.TextureLoader().load('perception/textures/sky.png');
      let texture_dn = new THREE.TextureLoader().load('perception/textures/sky.png');
      let texture_rt = new THREE.TextureLoader().load('perception/textures/sky.png');
      let texture_lf = new THREE.TextureLoader().load('perception/textures/sky.png');
        
      materialArray.push(new THREE.MeshBasicMaterial( { map: texture_ft }));
      materialArray.push(new THREE.MeshBasicMaterial( { map: texture_bk }));
      materialArray.push(new THREE.MeshBasicMaterial( { map: texture_up }));
      materialArray.push(new THREE.MeshBasicMaterial( { map: texture_dn }));
      materialArray.push(new THREE.MeshBasicMaterial( { map: texture_rt }));
      materialArray.push(new THREE.MeshBasicMaterial( { map: texture_lf }));
        
      for (let i = 0; i < 6; i++){
        materialArray[i].side = THREE.BackSide;
      }
        
      let skyboxGeo = new THREE.BoxGeometry( 1200, 1200, 1200);
      let skybox = new THREE.Mesh( skyboxGeo, materialArray );
      this.scene.add( skybox );
 
      let directionalLight = new THREE.DirectionalLight( 0xffffff, 0.75 );
      this.scene.add( directionalLight );
      let hemisLight = new THREE.HemisphereLight( 0xffffff, 0xffffff, 0.75 ); 
      this.scene.add( hemisLight );
      var ambientlight = new THREE.AmbientLight( 0x404040 ); // soft white light
      this.scene.add( ambientlight );

      let skyBoxGeometry = new THREE.CubeGeometry( 10000, 10000, 10000 );
      let skyBoxMaterial = new THREE.MeshBasicMaterial( { color: 0x9999ff, side: THREE.BackSide } );
      let skyBox = new THREE.Mesh( skyBoxGeometry, skyBoxMaterial );
      this.scene.add(skyBox);
      //this.scene.fog = new THREE.FogExp2( 0x9999ff, 0.00025 );      

      this.addGltftoScene();
    },
    animate() {
      requestAnimationFrame( this.animate );
      this.render();		
    },
    sniffer() {
      this.camera.updateMatrixWorld();
      document.addEventListener( 'keyup', (e)=>{
        switch (e.keyCode) {
          case 37:
            this.userinputs.push({
              "L":{
                "x":this.mesh.rotation.x*180/Math.PI,
                "y":this.mesh.rotation.y*180/Math.PI,
                "z":this.mesh.rotation.z*180/Math.PI
              }
            })
          break;
          case 38:
            this.userinputs.push({
              "U":{
                "x":this.mesh.rotation.x*180/Math.PI,
                "y":this.mesh.rotation.y*180/Math.PI,
                "z":this.mesh.rotation.z*180/Math.PI
              }
            })
          break;
          case 39:
            this.userinputs.push({
              "R":{
                "x":this.mesh.rotation.x*180/Math.PI,
                "y":this.mesh.rotation.y*180/Math.PI,
                "z":this.mesh.rotation.z*180/Math.PI
              }
            })
          break;
          case 40:
            this.userinputs.push({
              "D":{
                "x":this.mesh.rotation.x*180/Math.PI,
                "y":this.mesh.rotation.y*180/Math.PI,
                "z":this.mesh.rotation.z*180/Math.PI
              }
            })
          break;
        }   
      });
    },
    render() {
        this.renderer.render( this.scene, this.camera );
    },
    addGltftoScene(){
      // Instantiate a loader
      let loader = new GLTFLoader();

      // Optional: Provide a DRACOLoader instance to decode compressed mesh data
      var dracoLoader = new DRACOLoader();
      dracoLoader.setDecoderPath( '/examples/js/libs/draco/' );
      loader.setDRACOLoader( dracoLoader );
      // Load a glTF resource
      loader.load(
        // resource URL
        this.model,
        // called when the resource is loaded
        gltf => {
          this.scene.add( gltf.scene );
          gltf.animations; // Array<THREE.AnimationClip>
          gltf.scene; // THREE.Group
          gltf.scenes; // Array<THREE.Group>
          gltf.cameras; // Array<THREE.Camera>
          gltf.asset; // Object
          this.mesh = gltf.scene
        },
        // called while loading is progressing
        xhr => {
          console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );
        },
        // called when loading has errors
        error => {
          console.log( 'An error happened : ', error );
        }
      );
    }
  },
  mounted() {
    this.init();
    this.animate();
    this.update();
    this.sniffer();
    //init camera position to saved
  }
}
</script>

<style>
.size-threejs{
  height:50%;
  width:100%;
}
.size-tuto-img{
  height:200px;
  width:200px;
  margin:auto;
}
</style>