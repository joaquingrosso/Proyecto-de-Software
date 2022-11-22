<script setup>
    import Header from "./Header.vue"
</script>


<template>
  <Header/>
  
  {{ asocPorMes }}
  
  <Bar
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />

</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
import { mapActions, mapGetters } from 'vuex'
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: { Bar },
  props: {
    chartId: {
      type: String,
      default: 'bar-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 100
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      chartData: {
        labels: [ 'January', 'February', 'March' ],
        datasets: [ { data: [40, 20, 12] } ]
      },
      chartOptions: {
        responsive: true
      }
    }
  },
  computed: {
    ...mapGetters({
      asocPorMes: "auth/statsAsocXMes",
    })

  },
  methods: {
    ...mapActions("auth", ["asociadosInscriptosPorMes"]),
    async getAsociadosPorMes() {
      await this.asociadosInscriptosPorMes()
        .catch(() => {
          // Handle error
          this.error = true;
        });

    },
  },
  created() {
    this.getAsociadosPorMes();
  }
}

  



</script>