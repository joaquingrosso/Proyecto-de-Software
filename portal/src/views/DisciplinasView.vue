<script setup>
import Header from "./Header.vue"
</script>

<script >
import axios from 'axios'

export default {
  name: 'Main',
  data () {
    return {
        mensaje: ' '
      }
  },
  methods: {
    getMensaje () {
      const path = 'http://127.0.0.1:5000/api/club/disciplines'
      axios.get(path).then((respuesta) => {
        this.mensaje = respuesta.data
      })
      .catch((error) => {
        console.log(error)
      })
    }
  },
  created () {
    this.getMensaje()
  }
}

</script>



<template>

  <Header/>

  <div>
    <p>{{ mensaje }}</p>
  </div>
</template>

