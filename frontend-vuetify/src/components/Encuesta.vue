<template>
  <div >
    <v-progress-circular
      :size="70"
      :width="7"
      color="purple"
      indeterminate
      style="display: block; width: 100px; margin: 0 auto"
      v-if="!show"
    ></v-progress-circular>
    <v-container v-if="show">
      <div class="wordart slate"><span class="text">Votación</span></div>
    <v-row class="text-center">
      <v-col align="center">
        <BaseEncuesta :comentarios=comentarios_David_Larousse :imagen=imagen_david  :nombre=nombre_david />
      </v-col>
      <v-col align="center">
        <BaseEncuesta :comentarios=comentarios_Jonathan_Lowri :imagen=imagen_jonathan  :nombre=nombre_jonathan />
      </v-col>
    </v-row>
    </v-container>
  </div>
</template>

<style scoped>
@import "./css/encuesta.css";
</style>

<script>
import Api from "./Api";
import BaseEncuesta from "./BaseEncuesta";

export default {
  name: "Encuesta",
  components:{BaseEncuesta},
  data: () => ({
    comentarios_David_Larousse:[],
    nombre_david:"David Larousse",
    imagen_david:require('../assets/David Larousse.png'),
    comentarios_Jonathan_Lowri:[],
    nombre_jonathan:"Jonathan Lowrie",
    imagen_jonathan:require('../assets/Jonathan Lowrie.png'),
    show:false,
  }),
  methods:{
    getComentarios(){
      return Api.get("Comentarios/");
    }
  },
  created(){
    this.show =false
    this.getComentarios().then(response =>{
        response.data.filter(comentario =>{
          if(comentario.id_estrella.id==15){
            this.comentarios_David_Larousse.push(comentario)
          }
        }); 
      }).catch(error =>{
        alert("A ocurrido el siguiente error: "+ JSON.stringify(error.response.data))
      });
    this.getComentarios().then(response =>{
        response.data.filter(comentario =>{
          if(comentario.id_estrella.id==25){
            this.comentarios_Jonathan_Lowri.push(comentario)
            
          }
        }); 
        this.show = true;
      }).catch(error =>{
        alert("A ocurrido el siguiente error: "+ JSON.stringify(error.response.data))
      });
  },
};
</script>
