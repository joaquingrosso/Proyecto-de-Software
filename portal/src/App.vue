<script setup>
import { RouterLink, RouterView } from "vue-router";
</script>

<template>  

 <RouterView/>

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

  .nav_header ul a{  
    text-decoration: none;
    font-size: 1.5rem;
    color:rgb(255, 255, 255);
    font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
    letter-spacing: 1px;
    transition: all .3s ease;
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
    cursor: pointer;
  }


  .nav_header li:hover{
    scale: 1.05;
    transition: all .3s ease;
  }

  .nav_header ul a:hover{
    color: white;
    font-weight: bold;
    cursor: pointer;
    transition: all .3s ease;
  }




</style>