
<template>
    <div v-if="!error">

        <Pie :chart-options="chartOptions" :chart-data="chartData" :chart-id="chartId" :dataset-id-key="datasetIdKey"
            :plugins="plugins" :css-classes="cssClasses" :styles="styles" :width="width" :height="height" />
    </div>
    <div v-else>
        <br />
        <h1>El grafico de Pizza no se encuentra disponible</h1>
    </div>
</template>
  
<script>
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, CategoryScale, LinearScale, ArcElement, PieController } from 'chart.js'
import { mapActions, mapGetters } from 'vuex'
ChartJS.register(Title, Tooltip, Legend, CategoryScale, LinearScale, ArcElement, PieController)

export default {
    name: 'PieChart',
    components: { Pie },
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
            error: false,
            dic: {},
            chartData: {
                labels: ['Al Dia', 'Morosos'],
                datasets: [{
                    label: "Morosos y Al Dia",
                    data: [],
                    backgroundColor: [
                        'rgb(255, 99, 132)',
                        'rgb(54, 162, 235)'
                    ],
                    hoverOffset: 4
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
            asocMxAD: "auth/statsMorosAlDia",
        })

    },
    methods: {
        ...mapActions("auth", ["asociadosMorososAlDia"]),
        async getAsociadosMxAD() {
            await this.asociadosMorososAlDia()
                .catch(() => {
                    // Handle error
                    this.error = true;
                });
        },
        setDiccionario() {
            this.dic = this.asocMxAD;
            const lista = Object.values(this.dic);
            lista.forEach(element => {
                this.chartData.datasets[0].data.push(element);
            });
        }
    },
    created() {
        this.getAsociadosMxAD();
        this.setDiccionario();
    }
}


</script>