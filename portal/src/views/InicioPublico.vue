

<template>

    <div>
        <nav class="nav_bar">
      <div id="menu" class="nav_header">
        
        <ul>
          <RouterLink to="/cuotas">
            <li class="nav-item" @click="verCuotasUsuario">Estado de Cuotas</li>
          </RouterLink>
        </ul>

      </div>
    </nav>
    <Cuotas cuotas />
    </div>

</template>
<script>
import { mapActions , mapGetters } from 'vuex'
import Cuotas from '../components/Cuotas.vue';

export default {
    data: () => ({
        error: false,
        cuotas: {
            periodo: null,
            monto: null
        }
    }),
    computed: {
        ...mapGetters({
            cuotas: "auth/cuotas",
        })
    },
    methods: {
        ...mapActions("auth", ["cuotasUsuario"]),
        async verCuotasUsuario() {
            await this.cuotasUsuario(this.cuotas)
                .catch(() => {
                // Handle error
                this.error = true;
                
            });
        },
    },
    components: { Cuotas }
};

</script>