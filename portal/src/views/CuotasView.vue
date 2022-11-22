<script setup>
import Header from "./Header.vue"
</script>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    data: () => ({
        error: false,
        cuota: {},
        validarFecha: true,
        pago:{
            monto: null,
            periodo:null
        }
    }),
    computed: {
        ...mapGetters({
            cuotas: "auth/cuotas",
            disciplinaAsociado: "auth/disciplinasAsociado",
        })

    },

    methods: {
        ...mapActions("auth", ["cuotasUsuario","pagarCuotaAsociado"]),
        async verCuotasUsuario() {
            await this.cuotasUsuario()
                .catch(() => {
                    // Handle error
                    this.error = true;
                    this.validarFecha = false;
                    
                });

        },
        async pagarCuotas(periodo,monto){
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
        <div class="box_content_desc">
            <div class="col-md-10">
                <table class="table table-striped table-bordered" >
                    <thead>
                        <tr class="bg-primary text-white" align="center">
                            <th >Disciplina</th>
                            <th>Mes</th>
                            <th>Monto</th>
                            <th class="text-center">Operaciones</th>
                        </tr>
                    </thead>
                    <tbody id="myTable">
                        <tr v-for="valor, index in cuotas" align="center">
                            <td > {{disciplinaAsociado[index]?.name}}</td>
                            <td > {{ valor?.periodo }} </td>
                            <td > {{ valor?.monto }} </td>
                            <td > <button type="submit" class="btn btn-danger btn-md" v-if="valor?.estado == 'No-Paga'" @click="pagarCuotas(valor?.periodo,valor?.monto)"> Pagar</button></td>

                        </tr>

                    </tbody>
                </table>

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