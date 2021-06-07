import Vue from "vue";
import Router from "vue-router";
import Encuesta from "../components/Encuesta"
import Resultados from "../components/resultados"

Vue.use(Router);

export default new Router({
  routes: [
    {
    path: '/',
    name: 'Encuesta',
    component: Encuesta
    },
    {
      path: '/Resultados',
      name: 'Resultados',
      component: Resultados
    },

  ],
  mode: "history"
})