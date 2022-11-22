<script setup>
      import Header from "./Header.vue"
</script>

<template>
    <Header></Header>
        <div class="box_content_desc">
            <h1 class="title"> Descripcion </h1>
            <br>
            <div style=" height: auto; width: 1000px ">
            <h5>
            El Club deportivo Villa Elisa es una institución que actúa, fomenta 
            y desarrolla actividades deportivas.
            Persigue como objetivo fundamental ofrecer actividades recreativas y 
            atractivas para la sociedad que lo rodea, mediante la constante mejora en las actividades.
            </h5>
            </div>
        </div>

    
</template>

<style>

    .box_content_desc{
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }      

</style>