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
            <p style="justify-content:center ;">
            El Club deportivo Villa Elisa es una institución que actúa, fomenta 
            y desarrolla actividades deportivas.
            Persigue como objetivo fundamental ofrecer actividades recreativas y 
            atractivas para la sociedad que lo rodea, mediante la constante mejora en las actividades.<br/><br/>
            Dentro de esta pagina se podra visualizar:<br/><br/>
            <strong>
            *Todas las disciplinas del club.<br/>
            *Informacion de contacto<br/>
            *Estadisticas relacionadas a las disciplinas, asociados y cuotas.<br/><br/>
            </strong>
            Al Iniciar sesion se podran realizar operaciones como pagar las cuotas que el socio debe en un unico pago.
            Ademas de ver las disciplinas en las que se encuentra inscripto/a y tambien ver su carnet en forma digital.
        </p>
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