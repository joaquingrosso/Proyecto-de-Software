<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "./components/HelloWorld.vue";
</script>

<template>
  
  <!-- <header>
    <img
      alt="Vue logo"
      class="logo"
      src="@/assets/logo.svg"
      width="125"
      height="125"
    />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView /> -->

  <div id="cabecera" class="content">
    <div class="box_logo">
      <a href=""><img src="../public/img/logo2.png"></a>
    </div>
    <div class="box_title">
      <h1>Club Deportivo Villa Elisa</h1>
    </div>
    <div class="box_buttons">
      <a href=""><button type="button" class="btn btn-primary">Iniciar Sesion</button></a>
      <a href=""><button type="button" class="btn btn-primary">Registrarse</button></a>
    </div>
  
  </div>
  
  
  <!-- Menu -->
  
  
  <nav class="nav_bar">
    <div id="menu" class="nav_header">
  
      <ul>
        <li class="nav-item"><a class="nav-link" href="#">Inicio</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Disciplinas</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Contacto</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Descripcion</a></li>
      </ul>
  
    </div>
  </nav>
  
  
  <div class="box_content">
  <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="../../../public/img/image_slider/slider1.jpg" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="../../../public/img/image_slider/slider2.jpg" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="../public/img/image_slider/slider3.jpg" class="d-block w-100" alt="...">
      </div>
      <div class="carousel-item">
        <img src="../public/img/image_slider/slider4.jpg" class="d-block w-100" alt="...">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button>
  </div>
  </div>



</template>

<style>
  #cabecera{
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    position: relative;
    width: 100%;
    height: 11.5rem;
    padding: 0 1rem;
  }

  #carouselExampleControls{
    width: 50%;
    height: 50%;
    
  }

  .box_content{
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .box_logo img{
    width: 75%;
  }


  .box_title h1{
    font-size: 70px;
  }

  .box_buttons{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 1rem;

  }
  
  .box_buttons a{
    text-decoration: none;
  }



  .box_buttons button{
    width: 12rem;
    text-align: center;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
  }


  .btn-primary{
    font-size: 25px;
  }

  .nav_bar{
    border-top: 5px ridge rgb(3, 2, 2);
    margin: 1rem 0;
    padding: 1.5rem 0;
  }

  .nav_header ul{  
    list-style: none;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    gap: 2rem; 
    background-color: rgba(0, 0, 0, 0.068);
    padding: 1.7rem 0;
  }
  
  .nav_header li{  
    border: 2px solid rgb(0, 0, 0);
    width: 12rem;
    text-align: center;
    border-radius: 10px;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.842);

  }

  .nav-item a{
    font-size: 1.5rem;
    color:rgb(255, 255, 255);
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    letter-spacing: 1px;
    transition: all .3s ease;
  }

  .nav_header li:hover{
    scale: 1.05;
    transition: all .3s ease;
  }

  .nav-item a:hover{
    color: white;
    font-weight: bold;
    transition: all .3s ease;
  }




</style>