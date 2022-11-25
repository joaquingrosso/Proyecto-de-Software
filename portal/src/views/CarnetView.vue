<script setup>
import Header from "./Header.vue"
</script>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
    data: () => ({
        error: false,
    }),
    computed: {
        ...mapGetters({
            carnet: "auth/carnet",
        })
    },
    methods: {
        ...mapActions("auth", ["carnetAsociado"]),
        async verCarnetAsociado() {
            await this.carnetAsociado()
                .catch(() => {
                    // Handle error
                    this.error = true;

                });
        },
    },
    created() {
        this.verCarnetAsociado();
    }
};

</script>

<template>
    <Header></Header>
    <main>
        <div class="container">
            <div id="header">
                <div id="titulo">
                    <h1>Club Deportivo Villa Elisa</h1>
                </div>
            </div>
            <div id="body">
                <div id="img_estado">
                    <div><h3>Estado: </h3><h5>{{ carnet.description }}</h5>
                    </div>
                </div>
                <div>
                    <h3>{{carnet.profile.last_name}} {{carnet.profile.first_name}}</h3>
                    <h5>{{carnet.profile.document_type}}: {{carnet.profile.document_number}}</h5>
                    <h5># Socio: {{carnet.profile.number}}</h5>
                    <h5>Fecha Alta: {{carnet.profile.fecha_alta}}</h5>
                </div>
                <div v-if="error">No se encuentra disponible el Carnet Digital</div>

            </div>
        </div>
    </main>

</template>

<style>
.container {
    position: absolute;
    left: 35%;
    margin: 70px 0 0 -25px;
}

#header {
    border-color: black;
    border: 1mm solid;
    border-bottom: 1px solid;
    width: 50%;
}

#body {
    border-color: black;
    border: 1mm solid;
    width: 50%;
    display: flex;
}

#body img {
    width: 100px;
    height: 100px;
    border-radius: 1500px;
}

#titulo {
    text-align: center;

}

#body div {
    margin-left: 20%;
}
</style>