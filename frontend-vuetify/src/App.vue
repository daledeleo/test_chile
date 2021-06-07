<template>
  <v-app>
    <v-app-bar
      app
      color="#06a323"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Encuesta"
          class="shrink mr-2"
          contain
          src="https://uploads-blog.encuesta.com/wp-content/uploads/2015/04/31154320/concepto-encuesta-linea-personas-encuestas-lista-verificacion_25147-179.jpg"
          transition="scale-transition"
          width="40"
          style="border-radius: 50%;"
        />

        <p
          alt="Vuetify Name"
          class="shrink mt-1"
          contain
          min-width="100"
          width="100"
        >
        Encuesta para Null Valley - {{this.$route.name}}</p>
      </div>
    </v-app-bar>

    <v-main>
      <router-view> </router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>
