<script setup>
import Header from "./Header.vue"
</script>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    data: () => ({
        error: false,
        validarFecha: true,
    }),
    computed: {
        ...mapGetters({
            cuotas: "auth/cuotasImpagas",
            disciplinaAsociado: "auth/disciplinasAsociado",
        })

    },

    methods: {
        ...mapActions("auth", ["cuotasUsuarioImpagas", "pagarCuotaAsociado"]),
        async verCuotasUsuario() {
            await this.cuotasUsuarioImpagas()
                .catch(() => {
                    // Handle error
                    this.error = true;
                    this.validarFecha = false;
                });
        },

        async pagarCuota(cuota){
            await this.pagarCuotaAsociado(cuota)
        },
        async pagarCuotas(cuota) {
            for (let index = 0; index < cuota.disciplinas.length; index++) {
                cuota.disciplinas[index].cuotas.forEach(element => {
                    this.pagarCuota(element)
                });                
            }
            this.$router.push("/");
        },
        
    },
    created() {       
        this.verCuotasUsuario();
    }
};

</script>

<template>
    <Header></Header>
    <main>
        <div v-if="!error">
            <h1>Listado de cuotas</h1>
        <div class="accordion" id="accordionExample" >
            <div class="accordion-item" >
                <h2 class="accordion-header" id="headingOne">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse"
                        data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne" >
                        <h4>Resumen de Factura </h4>
                    </button>
                </h2>
                <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                    data-bs-parent="#accordionExample" v-for="valor in cuotas.disciplinas.length" >
                    <div class="accordion-body" >
                       <br/>
                        Nombre de Disciplina: {{cuotas.disciplinas[valor-1].nombre}}
                        <div v-if = "cuotas.disciplinas[valor-1].cuotas.length > 0 "  >
                            <div v-for="valor2 in cuotas.disciplinas[valor-1].cuotas.length">
                                Periodo a Pagar: {{cuotas.disciplinas[valor-1].cuotas[valor2-1].periodo}} -- Monto: {{cuotas.disciplinas[valor-1].cuotas[valor2-1].monto}}
                                
                            </div>
                        </div >
                        <div v-else>
                            No hay cuotas a pagar    
                        </div>
                    </div>
                </div>
                <div>
                    
                    <div v-if="cuotas.total_a_pagar != cuotas.monto_base">
                        Monto de la cuota del Club: {{cuotas.monto_base}} -- Total a Pagar: {{cuotas.total_a_pagar}}
                        <button type="submit" class="btn btn-danger btn-md" @click="pagarCuotas(cuotas)" > Pagar</button>
                    </div>
                        
                </div>

            </div>

        </div>
        
        </div>
        <div v-else>
            <h1>Upss Ocurrio un problema y no se cargo la vista de las cuotas pendientes</h1>
        </div>
        

    </main>

</template>

<style>
.box_content_desc {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
</style>