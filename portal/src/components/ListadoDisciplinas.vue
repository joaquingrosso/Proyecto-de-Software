<script>
import axios from "axios"
    export default {
        data(){
            return {
                  
                listItems: {}
                
            }
        },
        created() {
            // Produccion
           
            axios
            .get(`http://127.0.0.1:5000/api/club/disciplines`)
            .then((result) => {this.getData(result.data)})
            .catch( error => {console.log(error)})

        },
        methods:{
            async getData(disciplinas){
                // const res = await fetch('');
                // const resFech = res.json();
                // this.listItems = resFech;
                for (var j = 0; j < disciplinas.length; j++) {
                    const disciplina = {
                        id: disciplinas.id,
                        nombre: disciplinas.nombre,
                    }
                    this.listItems.append(disciplina);  
                    
        }
            }
        },

        // mounted(){
        //     this.getData()
        // }
    }
</script>
<template>
    <div v-for="item in listItems">
        {{item.nombre}}
    </div>
</template>