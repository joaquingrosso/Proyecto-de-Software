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
      path: "/inicioPublico",
      name: "inicioPublico",
      component: () => import("../views/InicioPublico.vue"),
    },
    {
      path: "/cuotas",
      name: "cuotas",
      component: () => import("../views/CuotasView.vue"),
    },
  ],
});

export default router;
