


<template>

  
  <div class="conteiner">
    <form>
      <div class="imge"><img src="../../public/img/logo2.png"></div>

      <h1 class="h3 mb-3 fw-normal">Inicio Sesion</h1>

      <input type="email" class="form-control" placeholder="Email" required>

      <input type="password" class="form-control" placeholder="Password" required>

      <button class="w-100 btn btn-lg btn-primary" type="submit">Iniciar sesion</button>
    </form>
  </div>
    
</template>

<style>

.conteiner {
  display: flex;
  justify-content: center;
  align-items: center;
  position:absolute;
  top:8rem;
  right:0px;
  left:0px;
}

.conteiner form{  
  width: 20%;
}

.conteiner .imge{  
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

.conteiner input{  
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px;
}

.conteiner h1{
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px;
}

.conteiner button{
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px;
}

</style>