<script setup>
import ListadoDisciplinas from "../components/ListadoDisciplinas.vue";
import axios from  "axios"
</script>

<template>
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

</style>