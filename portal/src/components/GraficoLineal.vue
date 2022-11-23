 
<template>
  <Line :chart-options="chartOptions" :chart-data="chartData" :chart-id="chartId" :dataset-id-key="datasetIdKey"
    :plugins="plugins" :css-classes="cssClasses" :styles="styles" :width="width" :height="height" />


</template>

<script>
import { Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, PointElement, LineElement } from 'chart.js'
import { mapActions, mapGetters } from 'vuex'
ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement)

export default {
  name: 'LinearChart',
  components: { Line },
  props: {
    chartId: {
      type: String,
      default: 'line-chart'
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
      dic: {},
      chartData: {
        labels: ['January','February','March','April','May','June','July','August','September','Octuber','November','December'],
        datasets: [{
          label: "ASOCIADOS POR AÑO",
          backgroundColor: "RED",
          borderColor: 'rgb(255, 115, 115)',
          data: [],
          pointBorderWidth: 10
        }]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,        
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
    setDiccionario() {
      this.dic = this.asocPorMes;
      const lista = Object.values(this.dic);
      lista.forEach(element => {
        this.chartData.datasets[0].data.push(element);
      });
    }
  },
  created() {
    this.getAsociadosPorMes();
    this.setDiccionario();
  }
}


</script>

  