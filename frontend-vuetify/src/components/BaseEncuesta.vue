<template>
  <div>
    <v-container>
      <v-row class="text-center">
        <v-col align="center">
          <v-img :src="imagen" contain height="200" width="200" />
          <Typical
            id="h3_votacion"
            class="typicalWrapper"
            :steps="[nombre, 1000]"
            :loop="3"
            :wrapper="'h2'"
          ></Typical>
          <br />
          <v-divider></v-divider>
          <h4 style="margin-bottom:10px">Comentarios</h4>
          <h6>Comentarios en total: {{comentarios.length}}</h6>
          <div class="div_comentarios">
            <v-row v-for="(comentario, index) in comentarios" :key="index">
              <v-card class="card_comentario" elevation="10">
                <v-card-text>
                  <v-avatar :color="comentario.color" size="20" class="white--text">
                    {{ getInitial(comentario.nickname) }}
                  </v-avatar>
                  <strong> {{ comentario.nickname }}</strong>
                  {{ comentario.comentario }}
                </v-card-text>

                <v-card-actions
                  >opinion:
                  <v-icon :color="comentario.color">
                    {{ getThumb(comentario.valoracion) }}</v-icon
                  ></v-card-actions
                >
              </v-card>
            </v-row>
          </div>
          
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

export default {
  name: "Encuesta",
  
  components: { Typical },
  props: {
    comentarios: Array,
    imagen: String,
    nombre: String
  },
  methods: {
    getThumb(valoracion) {
      var icon = "";
      if (valoracion > 0) {
        icon = "mdi-thumb-up";
      } else {
        icon = "mdi-thumb-down";
      }
      return icon;
    },
    genRandomIndex(length) {
      return Math.ceil(Math.random() * (length - 1));
    },
    getInitial(nombre) {
      return nombre[0];
    },
   
  },
};
</script>
