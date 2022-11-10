<script setup>
  import Header from "./Header.vue"
</script>

<template>
  <main>
    <Header/>

    <div class="box_content_inicio">

      <h1> Inicio </h1>

      <br>
      
      <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="../../public/img/image_slider/slider1.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="../../public/img/image_slider/slider2.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="../../public/img/image_slider/slider3.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="../../public/img/image_slider/slider4.jpg" class="d-block w-100" alt="...">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls"
          data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls"
          data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
      
    </div>
  </main>
</template>


<style>

  .box_content_inicio{
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
  }  

</style>