<script setup>
import Header from "../views/Header.vue"
</script>

<script >
import { mapActions, mapGetters } from 'vuex'
export default {
  data: () => ({
    error: false,
  }),
  computed: {
    ...mapGetters({
      cuotasPagas: "auth/pagosRealizados",
    })

  },
  methods: {
    ...mapActions("auth", ["verCuotaAsociado"]),
    async verPagosRealizados() {
      await this.verCuotaAsociado()
        .catch(() => {
          // Handle error
          this.error = true;

        });

    },
  },
  created() {
    this.verPagosRealizados();
  }
}
</script>

<template>
    <Header></Header>
    <div v-if="!error">
        <h1>Listado de cuotas Pagas</h1>
        <div class="accordion" id="accordionExample" v-for="valor in cuotasPagas.length" v-if="cuotasPagas.length > 0">
            <div class="accordion-item" >
                <h2 class="accordion-header" id="headingOne">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" >
                        <h4>{{cuotasPagas[valor-1].periodo}} </h4>
                    </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                    data-bs-parent="#accordionExample">
                    <div class="accordion-body" >
                        Monto: {{cuotasPagas[valor-1].monto}}
                    </div>
                </div>
            </div>  
        </div>
        <div v-else>
            <br/>
            <h2>No se registro ninguna cuota paga</h2>
        </div>
    </div>
    <div v-else>
        <h1>Upss Ocurrio un problema y no se cargo la vista de los pagos realizados</h1>
    </div>
        
        
</template>