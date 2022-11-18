<script setup>
import Header from "./Header.vue"
</script>

<script>
import { mapActions , mapGetters } from 'vuex'

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
    }
};

</script>

<template>
    <Header></Header>
    <main>
        <div class="box_content_desc">
            <div class="col-md-10">
                {{cuotas}}
                <table class="table table-striped table-bordered">
                    <thead>
                        <tr class="bg-primary text-white">
                            <th>Mes</th>
                            <th>Monto</th>
                            <th class="text-center">Operaciones</th>
                        </tr>
                    </thead>
                    <tbody id="myTable">
                        <tr v-for="(valor) in cuotas">
                            <td> {{valor.periodo}} </td>
                            <td> {{valor.monto}} </td>
                            <td> Operaciones </td>

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