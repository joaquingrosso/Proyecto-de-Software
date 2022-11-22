import { createRouter, createWebHistory } from "vue-router";
import InicioView from "../views/InicioView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "inicio",
      component: InicioView,
      // component: () => import("../views/AboutView.vue"),
    },
    // ruta al login
    {
      path: "/login",
      name: "login",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/disciplinas",
      name: "disciplinas",      
      component: () => import("../views/DisciplinasView.vue"),
    },
    {
      path: "/contacto",
      name: "contacto",      
      component: () => import("../views/ContactoView.vue"),
    },
    {
      path: "/estadistica",
      name: "estadistica",      
      component: () => import("../views/EstadisticaView.vue"),
    },
    {
      path: "/descripcion",
      name: "descripcion",      
      component: () => import("../views/DescripcionView.vue"),
    },
    {
      path: "/home",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/cuotas",
      name: "cuotas",
      component: () => import("../views/CuotasView.vue"),
    },
    {
      path: "/carnet",
      name: "carnet",
      component: () => import("../views/CarnetView.vue"),
    },
    {
      path: "/mis_disciplinas",
      name: "mis_disciplinas",
      component: () => import("../views/AsociadoDisciplinasView.vue"),
    },
    {
      path: "/estadisticas",
      name: "estadisticas",
      component: () => import("../views/EstadisticasView.vue"),
    },
  ],
});

export default router;
