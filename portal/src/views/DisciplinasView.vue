<!-- <script setup>
import ListadoDisciplinas from "../components/ListadoDisciplinas.vue";
import axios from  "axios"
</script> -->

<!-- <template>
    <main>
        <div class="box_content_disciplinas">
            <h1 class="title"> Disciplinas </h1>
                <ListadoDisciplinas/>
            <br>
        </div>
    </main>
    
</template>

<style>

    .box_content_disciplinas{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }  

</style> -->

<template>
  <div>
    <p>{{ mensaje }}</p>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Main',
  data () {
    return {
      // mensaje: ' '
      mensaje: ['nombre', 'instructores', 'monto'],
        id: "",
        nombre: "",
        instructores: "",
        monto: "",   
        postres: [], // Creamos este array para almacenar los datos JSON 
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