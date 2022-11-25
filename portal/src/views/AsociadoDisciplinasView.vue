<script setup>
import Header from "../views/Header.vue"
</script>

<script >
import { mapActions, mapGetters } from 'vuex'

export default {
  data: () => ({
    error: false,
  }),
  computed: {
    ...mapGetters({
      disciplinaAsociado: "auth/disciplinasAsociado",
    })
  },
  methods: {
    ...mapActions("auth", ["disciplinasAsociado"]),
    async verDisciplinasAsociado() {
      await this.disciplinasAsociado()
        .catch(() => {
          // Handle error
          this.error = true;

        });
    },
  },
  created() {
    this.verDisciplinasAsociado();
  }
};
</script>



<template>

  <Header />
  <div v-if="!error">
    <div className="container ">
      <div className="row">
        <div className="col-md-4" v-for="valor in disciplinaAsociado">
          <div className="card  animate__animated animate__fadeInUp">
            <div class="box-image">
              <img src="../../public/img/logo2.png" class="card-img-top" alt="...">
            </div>
            <div class="card-img-overlay">
              <div className="card-bodyy rounded">
                <h4 className="card-title text-center">{{ valor.name }}</h4>
                <p className="card-text text-dark text-center">Horario: {{ valor.date_time }}</p>
                <p className="card-text text-dark text-center">Instructores: {{ valor.instructors }}</p>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <h1>Upss Ocurrio un problema y no se cargo la vista de las disciplinas</h1>
  </div>

</template>

<style>
.card-img-top {
  width: 40%;
  opacity: 0.05;

}

.box-image {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.card {
  margin-bottom: 10px;
  background: #7CA0AF;

}

.card:hover {
  box-shadow: 5px 10px 20px 1px rgba(0, 0, 0, 0.959) !important;
  transition: all 0.7s linear;
}


.card-text {

  font-size: 1.5rem;
}
</style>

