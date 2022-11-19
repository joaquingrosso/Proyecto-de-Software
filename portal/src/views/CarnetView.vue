<script setup>
import Header from "./Header.vue"
</script>

<script>
import { mapActions, mapGetters } from 'vuex'

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
            console.log(this.cuotas);
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
        <div class="container">
            <div id="header">
                <div id="titulo">
                    <h1>Club Deportivo Villa Elisa</h1>
                </div>
            </div>
            <div id="body">
                <div id="img_estado">
                    <div>Estado: <h3>{{ estado }}</h3>
                    </div>
                </div>
                <div>
                    <h3></h3>
                    <h5></h5>
                    <h5># Socio: </h5>
                    <h5>Fecha Alta: </h5>
                    <div>
                        QR
                    </div>
                </div>

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