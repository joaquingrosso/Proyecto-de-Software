
<template>
  <div v-if="!error">

    <Bar :chart-options="chartOptions" :chart-data="chartData" :chart-id="chartId" :dataset-id-key="datasetIdKey"
      :plugins="plugins" :css-classes="cssClasses" :styles="styles" :width="width" :height="height" />

    <!-- para separar graficos -->
    <hr>
  </div>

  <div v-else>
    <br />
    <h1>El grafico de Barras no se encuentra disponible</h1>
  </div>


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
      default: 400
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
      default: () => {
      }
    },
    plugins: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      error: true,
      dic: {},
      chartData: {
        labels: [],
        datasets: [{
          label: "ASOCIADOS POR AÑO",
          backgroundColor: "BLUE",
          data: []
        }]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      }
    }
  },
  computed: {
    ...mapGetters({
      asocPorDisc: "auth/statsAsocXDisc",
    })

  },
  methods: {
    ...mapActions("auth", ["asociadosInscriptosPorDisciplina"]),
    async getAsociadosPorDisciplina() {
      await this.asociadosInscriptosPorDisciplina()
        .catch(() => {
          // Handle error
          this.error = true;
        });
    },
    setObject() {
      this.dic = this.asocPorDisc;
      const lista = Object.values(this.dic);
      const listaLabel = Object.keys(this.dic);
      lista.forEach(element => {
        this.chartData.datasets[0].data.push(element);
      });
      listaLabel.forEach(element => {
        this.chartData.labels.push(element);
      });
    }
  },
  created() {
    this.getAsociadosPorDisciplina();
    this.setObject();
  }
}


</script>