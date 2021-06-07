<template>
  <v-container>
    <div v-if="resultado != 'Empate'">
      <v-col align="center">
        <h1 style="text-align:center">
          <strong>Ganador</strong> con {{ total_votaciones }} votaciones
          (positivas/negativas).
        </h1>
        <v-img :src="imagen" contain height="200" width="200" />
        <Typical
          id="h3_votacion"
          class="typicalWrapper"
          :steps="[nombre, 1000]"
          :loop="3"
          :wrapper="'h2'"
        ></Typical>
      </v-col>
    </div>
    <div v-else>
      <h1 style="text-align:center"><strong>Empate</strong></h1>
      <v-row class="text-center">
        <v-col align="center">
          <strong>Ganador</strong> con {{ Jonathan_vataciones }} votaciones
          <v-img :src="imagenes[0]" contain height="200" width="200" />
          <Typical
            id="h3_votacion"
            class="typicalWrapper"
            :steps="[nombres[0], 1000]"
            :loop="3"
            :wrapper="'h2'"
          ></Typical>
        </v-col>
        <v-col align="center">
          <strong>Ganador</strong> con {{ David_votaciones }} votaciones
          <v-img :src="imagenes[1]" contain height="200" width="200" />
          <Typical
            id="h3_votacion"
            class="typicalWrapper"
            :steps="[nombres[1], 1000]"
            :loop="3"
            :wrapper="'h2'"
          ></Typical>
        </v-col>
      </v-row>
    </div>
    <br />
    <v-divider></v-divider>
    <div>
      <h4 style="text-align:center;">Opiniones con palabras ofuscadas</h4>
      <h6 style="text-align:center;">
        Catidad de Opiniones ofuscadas: {{ comentarios_ofuscados.length }}
      </h6>
      <div class="div_comentarios">
        <v-row
          v-for="(comentario, index) in comentarios_ofuscados"
          :key="index"
        >
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
    </div>
    <v-col align="center">
      <v-tooltip bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            color="primary"
            dark
            v-bind="attrs"
            v-on="on"
            @click="borrarComentarios"
          >
            Resturar encuesta
          </v-btn>
        </template>
        <span
          >Esto resturará la encuesta y borrará el listados de las opniones
          ofuscadas</span
        >
      </v-tooltip>
    </v-col>
  </v-container>
</template>

<script>
import Typical from "vue-typical";
import Api from "./Api";

export default {
  name: "Ganador",
  components: { Typical },

  props: {
    comentarios: Array
  },
  data: () => ({
    resultado: "",
    total_votaciones: 0,
    Jonathan_vataciones: 0,
    David_votaciones: 0,
    nombre: "",
    imagen: "",
    imagenes: [],
    nombres: [],
    comentarios_ofuscados: []
  }),
  methods: {
    borrarComentarios() {
      Api.delete("Comentarios/delete").then((response)=>{
          alert(response.data+', acontinuación será redireccionado a la pagina de Votación...');
          this.$router.replace({"name":"Encuesta"})
      }).catch(error=>{
          alert('A ocurrido el siguiente error: '+ JSON.stringify(error.response.data))
      });
    },
    includes(string) {
      var palabras_ofuscadas = [
        "Manzana",
        "coliflor",
        "bombilla",
        "derecha",
        "izquierda",
        "rojo",
        "azul"
      ];
      var cantidad = 0;
      palabras_ofuscadas.forEach(palabra => {
        if (string.includes(palabra)) {
          cantidad = cantidad + 1;
        }
      });
      return cantidad > 0;
    },
    getInitial(nombre) {
      return nombre[0];
    },
    getThumb(valoracion) {
      var icon = "";
      if (valoracion > 0) {
        icon = "mdi-thumb-up";
      } else {
        icon = "mdi-thumb-down";
      }
      return icon;
    }
  },

  created() {
    if (this.$props.comentarios.length < 0) {
      this.$router.replace({ "path": "/" });
    }
    this.$props.comentarios.forEach(comentario => {
      if (comentario.id_estrella.id == 15) {
        //David
        this.David_votaciones = this.David_votaciones + parseInt(incomentario.valoracion);
      }
      if (comentario.id_estrella.id == 25) {
        //Jonathan
        this.Jonathan_vataciones =
          this.Jonathan_vataciones +  parseInt(incomentario.valoracion);
      }
      if (this.includes(comentario.comentario)) {
        this.comentarios_ofuscados.push(comentario);
      }
    });

    if (this.Jonathan_vataciones > this.David_votaciones) {
      this.total_votaciones = this.Jonathan_vataciones;
      this.resultado = "Ganador";
      this.nombre = "Jonathan Lowrie";
      this.imagen = require("../assets/Jonathan Lowrie.png");
    } else if (this.David_votaciones > this.Jonathan_vataciones) {
      this.total_votaciones = this.David_votaciones;

      this.resultado = "Ganador";
      this.nombre = "David Larousse";
      this.imagen = require("../assets/David Larousse.png");
    } else {
      this.resultado = "Empate";
      this.imagenes.push(require("../assets/Jonathan Lowrie.png"));
      this.imagenes.push(require("../assets/David Larousse.png"));
      this.nombres.push("Jonathan Lowrie");
      this.nombres.push("David Larousse");
    }
  }
};
</script>