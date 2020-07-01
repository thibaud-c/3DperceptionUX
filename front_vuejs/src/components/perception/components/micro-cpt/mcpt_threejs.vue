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
  #threecontainer
</template>

<script>
import * as THREE from  'three/build/three.js'
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/examples/jsm/loaders/DRACOLoader.js';

export default {
  name: 'micro-component-threejs',
  props:['model', 'view','angles'],
  data () {
    return {
      camera: null,
      userinputs: [],
      scene: null,
      renderer: null,
      mesh: null,
      controls:null,
      d_time:null,
      d_start_coord:[],
      d_block_inputs:true,
      u_time:null,
      u_start_coord:[],
      u_block_inputs:true,
      l_time:null,
      l_start_coord:[],
      l_block_inputs:true,
      r_time:null,
      r_start_coord:[],
      r_block_inputs:true,
      first_input_time:null,
      first_input:true,
      last_input_time:null,
    }
  },
  methods: {
    init() {
      // set three windnullw responsive size
      let width = window.innerWidth
      let height = window.innerHeight
      let width_container = height*0.60                       
      let height_container=width*0.35

      let container = document.getElementById('threecontainer');

      this.scene = new THREE.Scene();
      this.camera = new THREE.PerspectiveCamera(70, height_container/width_container, 0.01, 1200);
      this.camera.position.x = 0;
      this.camera.position.y = 0;
      this.camera.position.z = this.view["z"];
      this.scene.add(this.camera)

      this.renderer = new THREE.WebGLRenderer({antialias: true});
      this.renderer.setSize(height_container, width_container);
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
    update() {
      this.camera.updateMatrixWorld();
      document.addEventListener( 'keyup', (e)=>{
        this.last_input_time=new Date();
        switch (e.keyCode) {
          case 37:
            //** right **//
            this.userinputs.push({
              "input_type":"right",
              "input_duration": (new Date()).getTime() - this.r_time.getTime(), 
              "start_coord":{
                "y":this.r_start_coord[0],
                "x":this.r_start_coord[1],
              },
              "end_coord":{
                "y":this.mesh.rotation.x*180/Math.PI,
                "x":this.mesh.rotation.y*180/Math.PI,
              }
            });
            this.r_block_inputs=true;
            break;
          case 38:
            //** down **//
            this.userinputs.push({
              "input_type":"down",
              "input_duration": (new Date()).getTime() - this.d_time.getTime(), 
              "start_coord":{
                "y":this.d_start_coord[0],
                "x":this.d_start_coord[1],
              },
              "end_coord":{
                "y":this.mesh.rotation.x*180/Math.PI,
                "x":this.mesh.rotation.y*180/Math.PI,
              }
            });
            this.d_block_inputs=true;
            break;
          case 39:
            //** left **//
            this.userinputs.push({
              "input_type":"left",
              "input_duration": (new Date()).getTime() - this.l_time.getTime(), 
              "start_coord":{
                "y":this.l_start_coord[0],
                "x":this.l_start_coord[1],
              },
              "end_coord":{
                "y":this.mesh.rotation.x*180/Math.PI,
                "x":this.mesh.rotation.y*180/Math.PI,
              }
            });
            this.l_block_inputs=true;
            break;
          case 40:
            //** up **//
            this.userinputs.push({
              "input_type":"up",
              "input_duration": (new Date()).getTime() - this.u_time.getTime(), 
              "start_coord":{
                "y":this.u_start_coord[0],
                "x":this.u_start_coord[1],
              },
              "end_coord":{
                "y":this.mesh.rotation.x*180/Math.PI,
                "x":this.mesh.rotation.y*180/Math.PI,
              }
            });
            this.u_block_inputs=true;
            break;
        }
      });
      document.addEventListener( 'keydown', (e)=>{
        if(this.first_input){
          this.first_input_time= new Date();
          this.first_input=false;
        }
        switch (e.keyCode) {
          case 37:
            //** right **//
            //Start sniffer
            if(this.r_block_inputs){
              this.r_block_inputs=false;
              this.r_time = new Date(),
              this.r_start_coord = [this.mesh.rotation.x*180/Math.PI,this.mesh.rotation.y*180/Math.PI];
            }
            //rotate
            this.mesh.rotation.y -= 0.1;
            break;
          case 38:
            //** down **//
            //Start sniffer
            if(this.d_block_inputs){
              this.d_block_inputs=false;
              this.d_time = new Date(),
              this.d_start_coord = [this.mesh.rotation.x*180/Math.PI,this.mesh.rotation.y*180/Math.PI];
            }
            //rotate
            this.mesh.rotation.x -= 0.1;
            if(this.mesh.rotation.x < 0.0001){this.mesh.rotation.x = 0.0001}
            break;
          case 39:
            //** left **//
            //Start sniffer
            if(this.l_block_inputs){
              this.l_block_inputs=false;
              this.l_time = new Date(),
              this.l_start_coord = [this.mesh.rotation.x*180/Math.PI,this.mesh.rotation.y*180/Math.PI];
            }
            //rotate
            this.mesh.rotation.y += 0.1;
            break;
          case 40:
            //** up **//
            //Start sniffer
            if(this.u_block_inputs){
              this.u_block_inputs=false;
              this.u_time = new Date(),
              this.u_start_coord = [this.mesh.rotation.x*180/Math.PI,this.mesh.rotation.y*180/Math.PI];
            }
            //rotate
            this.mesh.rotation.x += 0.1;
            if(this.mesh.rotation.x > 0.78){this.mesh.rotation.x = 0.78}
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
          //Set random camera rotation
          this.cameraset();
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
    },
    cameraset(){
      this.mesh.rotation.x = this.angles[0];
      this.mesh.rotation.y = this.angles[1];
      this.mesh.rotation.z = 0;
    }
  },
  mounted() {
    this.init();
    this.animate();
    this.update();
  }

}
</script>

<style>
</style>