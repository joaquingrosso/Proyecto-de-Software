<script setup>
import Header from "./Header.vue"
</script>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    data: () => ({
        error: false,
        cuota: {},
    }),
    computed: {
        ...mapGetters({
            cuotas: "auth/cuotas",
            disciplinaAsociado: "auth/disciplinasAsociado",
        })

    },
    methods: {
        ...mapActions("auth", ["cuotasUsuario"]),
        async verCuotasUsuario() {
            await this.cuotasUsuario()
                .catch(() => {
                    // Handle error
                    this.error = true;
                });

        },
        
    },
    created() {
        this.verCuotasUsuario();
        console.log(this.lista)
    }
};

</script>

<template>
    <Header></Header>
    <main>
        {{disciplinaAsociado}}
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
                            <td > <button type="submit" class="btn btn-danger btn-md"> Pagar</button></td>

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