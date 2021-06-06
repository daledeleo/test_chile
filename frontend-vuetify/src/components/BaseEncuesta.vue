<template>
  <div>
    <v-container>
    <v-row class="text-center">
      <v-col align="center">
        <v-img
          :src=imagen
          contain
          height="200"
          width="200"
        />
        <Typical
        id="h3_votacion"
        class="typicalWrapper"
        :steps="[nombre, 1000]"
        :loop=3
        :wrapper="'h2'"
      ></Typical>
      <br/>
      <p>Comentarios</p>
      <v-virtual-scroll
      :items="comentarios"
      :item-height="50"
      height="300"
    >
      <template v-slot:default="{ item }">
        <v-list-item>
            <!--
          <v-list-item-avatar>
            <v-avatar
              :color="item.color"
              size="56"
              class="white--text"
            >
              {{ item.initials }}
            </v-avatar>
          </v-list-item-avatar>
            -->
          <v-list-item-content>
            <v-list-item-title>{{ item.nickname }}</v-list-item-title>
            <v-list-item-subtitle>{{item.comentario}}</v-list-item-subtitle>
            <v-list-item-subtitle>{{item.valoracion}}</v-list-item-subtitle>
            <v-list-item-subtitle>{{item.id_estrella}}</v-list-item-subtitle>
          </v-list-item-content>

          <v-list-item-action>
            <v-btn
              depressed
              small
            >
              View User

              <v-icon
                color="orange darken-4"
                right
              >
                mdi-open-in-new
              </v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
      </template>
    </v-virtual-scroll>
      </v-col>
    </v-row>
    </v-container>
  </div>
</template>

<style scoped>
@import "./css/encuesta.css";
</style>

<script>
import Typical from "vue-typical";
import Api from "./Api";

export default {
  name: "Encuesta",
  components:{Typical},
  props:{
      comentarios:Array,
      imagen:String,
      nombre:String,
  },
  data: () => ({
        colors: ['#2196F3', '#90CAF9', '#64B5F6', '#42A5F5', '#1E88E5', '#1976D2', '#1565C0', '#0D47A1', '#82B1FF', '#448AFF', '#2979FF', '#2962FF'],
  }),
  methods:{
      genRandomIndex (length) {
        return Math.ceil(Math.random() * (length - 1))
      },
    getComentarios(id){
      var comentarios;
      Api.get("Comentarios/").then(response =>{
        comentarios = response.data.filter(comentario =>{
          if(comentario.id_estrella===id){
            return comentario
          }
        }); // David
      }).catch(error =>{
        alert("A ocurrido el siguiente error: "+ JSON.stringify(error.response.data))
      });
      return comentarios
    }
  },
  created(){
    this.comentarios_David_Larousse = this.getComentarios(15);
    this.comentarios_Jonathan_Lowri = this.getComentarios(25);
  },
};
</script>
