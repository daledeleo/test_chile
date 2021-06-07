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
      <div class="wordart slate"><span class="text">Resultados</span></div>
      <p class="p_text">
        Al parecer ya se llego al 50% de las votaciones de la población de Null
        Valley (10 votos)
      </p>
      <div>
        <Ganador :comentarios="comentarios" />
      </div>
    </v-container>
  </div>
</template>

<style scoped>
@import "./css/resultados.css";
</style>
<script>
import Ganador from "./Ganador";
import Api from "./Api";

export default {
  name: "resultados",
  components: { Ganador },
  data: () => ({
    comentarios: [],
    show: false
  }),
  created() {
    this.show = false;
    Api.get("Comentarios/")
      .then(response => {
        this.comentarios = response.data;
        if (this.comentarios.length < 10) {
          this.$router.replace({ path: "/" });
        }
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