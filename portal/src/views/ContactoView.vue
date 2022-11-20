<script setup>
  import Header from "./Header.vue"
</script>

<template>
    <Header></Header>
    <main>
        <div class="box_content_contacto">
            <h1 class="title"> Contacto </h1>
            <br>
            <h3> Email : {{ info.email }}</h3>
            <h3> Telefono: {{ info.telefono }} </h3>
        </div>
    </main>
    
</template>

<script >
import axios from 'axios'

export default {
  data() {
    return {
      info: {
        email : null,
        telefono: null
      },
    }
  },
  methods: {
    getInfo() {
      const path = 'http://127.0.0.1:5000/api/club/info'
      axios.get(path).then((respuesta) => {
        this.info.email = respuesta.data.email;
        this.info.telefono = respuesta.data.phone;
      })
        .catch((error) => {
          console.log(error)
        })
    },

  },
  created() {
    this.getInfo()
    console.log(this.info)
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