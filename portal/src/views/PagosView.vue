<script setup>
import Header from "./Header.vue"
</script>

<script >
import axios from 'axios'

export default {
  data () {
    return {
        lista:[],
      }
  },
  methods: {
    getMensaje () {
      const path = 'http://127.0.0.1:5000/api/club/disciplines'
      axios.get(path).then((respuesta) => {
        this.lista = respuesta.data;
      })
      .catch((error) => {
        console.log(error)
      })
    },

  },
  created () {
    this.getMensaje()
  }
}

</script>



<template>

  <Header/>

  <p>Pagos</p>    
          
</template>

<style>

</style>