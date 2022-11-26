<script setup>
  import Header from "./Header.vue"
</script>

<template>
    <Header></Header>
    <main>
        <div v-if="!error">
          <div class="box_content_contacto">
            <h1 class="title"> Contacto </h1>
            <br>
            <h3> Email : {{ contacto.email }}</h3>
            <h3> Telefono: {{ contacto.phone }} </h3>
        </div>
        </div>
        <div v-else>
            <h1>Upss Ocurrio un problema y no se cargo la informacion del Contacto del Club</h1>
        </div>
    </main>
    
</template>

<script >
import { mapActions, mapGetters } from 'vuex'
export default {
  data() {
    return {
      error: false,
    }
  },
  computed: {
    ...mapGetters({
      contacto: "auth/contacto",
    })

  },
  methods: {
    ...mapActions("auth", ["infoContacto"]),
    async verContacto() {
      await this.infoContacto()
        .catch(() => {
          // Handle error
          this.error = true;

        });

    },
  },
  created() {
    this.verContacto()
    }
}

</script>

<style>

    .box_content_contacto{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }      

</style>