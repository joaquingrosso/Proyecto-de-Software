 
<template>
    <Line
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
  import { Line } from 'vue-chartjs'
  import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, LineElement} from 'chart.js'
  import { mapActions, mapGetters } from 'vuex'
  ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale)
  
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
          labels: [ 'Hola Mundo' ],
          datasets: [ {
            label: "ASOCIADOS POR DISCIPLINA",
            // backgroundColor: "BLUE",
            data: [] } ]
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
      setDiccionario(){
        this.dic = this.asocPorDisc;
        const lista = Object.values(this.dic);
        console.log(lista);
        lista.forEach(element => {
          this.chartData.datasets[0].data.push(element);
        });
      }
    },
    created() {
      this.getAsociadosPorDisciplina();
      this.setDiccionario();
    }
  }
  
    
  </script>