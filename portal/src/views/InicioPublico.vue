

<template>

    <div>
        <!-- <nav class="nav_bar">
      <div id="menu" class="nav_header">
        
        <ul>
          <RouterLink to="/cuotas">
            <li class="nav-item" @click="verCuotasUsuario">Estado de Cuotas</li>
          </RouterLink>
        </ul>

      </div>
    </nav> -->

    <div class="col-md-10">
        <table class="table table-striped table-bordered">
            <thead>
                <tr class="bg-primary text-white">
                    <th>Mes</th>
                    <th>Monto</th>
                    <th class="text-center">Operaciones</th>
                </tr>
            </thead>
            <tbody id="myTable">
                <tr >
                    <td> {{cuotas.periodo}}</td>
                    <td> {{cuotas.monto}} </td>
                    <td>  </td>

                </tr>

            </tbody>
        </table>

      </div> 
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
    created () {
    this.verCuotasUsuario()
  }
};

</script>