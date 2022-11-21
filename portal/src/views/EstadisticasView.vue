<script setup>
// import { Bar } from 'vue-chartjs'
</script>

<template>
<h3>Cantidad de Disciplinas por asociado</h3>
<div className="col-md-4" v-for="valor in disciplinas">
    <h4>{{ valor.nombre }}</h4>
</div>
    <BarChart />
  </template>
<!--   
  <script>
  import BarChart from '../components/Bar.vue'
  
  export default {
    components: { BarChart }
  }
  </script>
 -->

 <script >
import { mapActions, mapGetters } from 'vuex'
export default {
  data: () => ({
    error: false,
  }),
  computed: {
    ...mapGetters({
      disciplinas: "auth/disciplinas",
    })

  },
  methods: {
    ...mapActions("auth", ["disciplinasClub"]),
    async verDisciplinas() {
      await this.disciplinasClub()
        .catch(() => {
          // Handle error
          this.error = true;

        });

    },
  },
  created() {
    this.verDisciplinas();
  }
}
</script>
