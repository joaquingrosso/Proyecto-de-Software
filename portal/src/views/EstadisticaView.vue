<script setup>
    import Header from "./Header.vue"
</script>


<template>
  <Header/>
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
      default: 100
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
      dic: {},
      chartData: {
        labels: [ 'January','February','March','April','May','June','July','August','September','Octuber','November','December' ],
        datasets: [ { data: [] } ]
      },
      chartOptions: {
        responsive: false
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
    setDiccionario(){
      this.dic = this.asocPorMes;
      const lista = Object.values(this.dic);
      console.log(lista);
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