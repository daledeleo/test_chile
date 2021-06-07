<template>
  <div>
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
          <BaseEncuesta
            :comentarios="comentarios_David_Larousse"
            :imagen="imagen_david"
            :nombre="nombre_david"
          />
        </v-col>
        <v-col align="center">
          <BaseEncuesta
            :comentarios="comentarios_Jonathan_Lowri"
            :imagen="imagen_jonathan"
            :nombre="nombre_jonathan"
          />
        </v-col>
      </v-row>
      <br />
      <v-divider></v-divider>
      <h4 style="margin-bottom:10px; text-align:center;">
        Registre su comentario
      </h4>
      <div class="div_form">
        <form>
          <v-text-field
            v-model="nickname"
            :error-messages="nicknameErrors"
            :counter="8"
            label="Nickname"
            required
            @input="$v.nickname.$touch()"
            @blur="$v.nickname.$touch()"
          ></v-text-field>
          <v-select
            v-model="select_valoracion"
            :items="items_valoracion"
            :error-messages="selectErrors"
            label="Valoración"
            required
            @change="$v.select_valoracion.$touch()"
            @blur="$v.select_valoracion.$touch()"
          ></v-select>
          <v-container fluid>
            <v-textarea
              counter
              :error-messages="comentarioErrors"
              clearable
              clear-icon="mdi-close-circle"
              label="Escriba su comentario"
              v-model="comentario"
              @change="$v.comentario.$touch()"
              @blur="$v.comentario.$touch()"
            ></v-textarea>
          </v-container>
          <v-select
            v-model="select_estrella"
            :items="items_estrelass"
            :error-messages="selectErrors_estrella"
            label="Escoga su estrella"
            required
            @change="$v.select_estrella.$touch()"
            @blur="$v.select_estrella.$touch()"
          ></v-select>
          <v-btn class="mr-4" @click="submit" color="primary">
            Registrar comentario
          </v-btn>
          <v-btn @click="clear" color="error">
            Limpiar formulario
          </v-btn>
        </form>
      </div>
    </v-container>
  </div>
</template>

<style scoped>
@import "./css/encuesta.css";
</style>

<script>
import Api from "./Api";
import BaseEncuesta from "./BaseEncuesta";
import { validationMixin } from "vuelidate";
import { required, maxLength } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],
  validations: {
    nickname: { required, maxLength: maxLength(8) },
    select_valoracion: { required },
    select_estrella: { required },
    comentario: { required,  maxLength: maxLength(120) }
  },
  name: "Encuesta",
  components: { BaseEncuesta },
  data: () => ({
    comentarios_David_Larousse: [],
    nombre_david: "David Larousse",
    imagen_david: require("../assets/David Larousse.png"),
    comentarios_Jonathan_Lowri: [],
    nombre_jonathan: "Jonathan Lowrie",
    imagen_jonathan: require("../assets/Jonathan Lowrie.png"),
    show: false,

    nickname: "",
    select_valoracion: null,
    items_valoracion: ["Negativa", "Positiva"],
    select_estrella: null,
    items_estrelass: ["David Larousse", "Jonathan Lowrie"],
    comentario: "",
  }),
  methods: {
    getComentarios() {
      return Api.get("Comentarios/");
    },
    submit() {
      this.$v.$touch();
      var form={
        nickname:this.nickname,
        comentario:this.comentario,
        valoracion: this.select_valoracion == this.items_valoracion[0]? -2:1,
        color: this.select_valoracion == this.items_valoracion[0] ? "red":"blue",
        id_estrella:this.select_estrella == "David Larousse" ? 15: 25,
      }
      Api.post('Comentarios/',form).then(() =>{
        alert("Exito en registrar su comentario a continuación se procederá a recargar la página.");
        this.$router.go();
      }).catch(error=>{
        alert("Ha ocurrido el siguiente error: "+JSON.stringify(error.response.data))
      })
    },
    clear() {
      this.$v.$reset();
      this.nickname = "";
      this.select_valoracion = null;
      this.select_estrella = null;
    }
  },

  computed: {
    comentarioErrors() {
      const errors = [];
      if (!this.$v.comentario.$dirty) return errors;
      !this.$v.comentario.maxLength &&
        errors.push(
          "El comentario solo debe de tener 120 caracteres incluidos los espacios."
        );
      !this.$v.comentario.required &&
        errors.push("Debe de comentar para enviar su votación.");
      return errors;
    },
    selectErrors() {
      const errors = [];
      if (!this.$v.select_valoracion.$dirty) return errors;
      !this.$v.select_valoracion.required &&
        errors.push("Debe de seleccionar una valoración.");
      return errors;
    },
    nicknameErrors() {
      const errors = [];
      if (!this.$v.nickname.$dirty) return errors;
      !this.$v.nickname.maxLength &&
        errors.push("nickname debe de tener máximo 8 caracters y minimo 6.");
      !this.$v.nickname.required && errors.push("nickname es requerido.");
      return errors;
    },
    selectErrors_estrella() {
      const errors = [];
      if (!this.$v.select_estrella.$dirty) return errors;
      !this.$v.select_estrella.required &&
        errors.push("Debe de seleccionar una valoración.");
      return errors;
    }
  },
  created() {
    this.show = false;
    this.getComentarios()
      .then(response => {
        if(response.data.length >= 10){
          this.$router.replace({"name":"Resultados"})
        }
        response.data.filter(comentario => {
          if (comentario.id_estrella.id == 15) {
            this.comentarios_David_Larousse.push(comentario);
          }
        });
      })
      .catch(error => {
        alert(
          "A ocurrido el siguiente error: " +
            JSON.stringify(error.response.data)
        );
      });
    this.getComentarios()
      .then(response => {
        response.data.filter(comentario => {
          if (comentario.id_estrella.id == 25) {
            this.comentarios_Jonathan_Lowri.push(comentario);
          }
        });
        this.show = true;
      })
      .catch(error => {
        alert(
          "A ocurrido el siguiente error: " +
            JSON.stringify(error.response.data)
        );
      });
  }
};
</script>
