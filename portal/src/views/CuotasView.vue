<script setup>
import Header from "./Header.vue"
</script>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    data: () => ({
        error: false,
        cuotaImpaga: {},
        validarFecha: true,
        pago: {
            monto: null,
            periodo: null
        }
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
        async pagarCuotas(periodo, monto) {
            this.pago.periodo = periodo;
            this.pago.monto = monto;
            await this.pagarCuotaAsociado(this.pago)

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
        <!-- <div class="box_content_desc">
            <div class="col-md-10">
                <table class="table table-striped table-bordered" >
                    <thead>
                        <tr class="bg-primary text-white" align="center">
                            <th >Cuota Societaria</th>
                            <th>Mes</th>
                            <th>Monto</th>
                            <th class="text-center">Operaciones</th>
                        </tr>
                    </thead>
                    <tbody id="myTable">
                        <tr v-for="valor, index in cuotas" align="center">
                            <td > {{valor.monto_cuota}}</td>
                            <td >  </td>
                            <td >  </td>
                            <td > <button type="submit" class="btn btn-danger btn-md" v-if="valor?.estado == 'No-Paga'" @click="pagarCuotas(valor?.periodo,valor?.monto)"> Pagar</button></td>

                        </tr>

                    </tbody>
                </table>

            </div> 
        </div> -->

        <!-- {{cuotas.disciplinas[1].nombre}}<br />
        {{cuotas.monto_base}}<br />
        {{cuotas.disciplinas[1].cuotas[1].monto}}<br />
        {{cuotas.disciplinas[1].cuotas[1].periodo}}<br />
        {{cuotas.disciplinas[1].cuotas[1].estado}}<br /> -->
        
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
                    data-bs-parent="#accordionExample" v-for="valor in cuotas.disciplinas.length">
                    <div class="accordion-body">
                       <br/>
                        Nombre de Disciplina: {{cuotas.disciplinas[valor-1].nombre}}
                        <div v-for="valor2 in cuotas.disciplinas[valor-1].cuotas.length">
                            Periodo a Pagar: {{cuotas.disciplinas[valor-1].cuotas[valor2-1].periodo}} -- Monto: {{cuotas.disciplinas[valor-1].cuotas[valor2-1].monto}}<br />
                            
                        </div>
                        
                    </div>
                </div>
                Monto de la cuota del Club: {{cuotas.monto_base}}
                
            </div>
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