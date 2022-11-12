


<!-- <template>

  
  <div class="conteiner">
    <form @submit.prevent="login" >

      <div class="imge"><img src="../../public/img/logo2.png"></div>

      <h1 class="h3 mb-3 fw-normal">Inicio Sesion</h1>

      <input v-model="email" type="email" class="form-control" placeholder="Email" required>

      <input v-model="password"  type="password" class="form-control" placeholder="Password" required>

      <button class="w-100 btn btn-lg btn-primary" type="submit">Iniciar sesion</button>
    </form>
  </div>
    
</template> -->

<template>
  
  
    <form action class="form" @submit.prevent="login">
      <label class="form-label" for="#user.email">Email:</label>
      <input v-model="user.email" placeholder="Email" class="form-input" type="email" id="email" required>
      <label class="form-label" for="#user.password">Password:</label>
      <input v-model="user.password" placeholder="Password" type="password" autocomplete="on" class="form-input" id="password" required>
      <p v-if="error" class="error">Has introducido mal el email o la contraseña.</p>
      <input class="form-submit" type="submit" value="Login">
    </form>
</template>

<script>

import { mapActions, mapGetters } from 'vuex'
  export default {
    name: 'LoginView',
    data: () => ({
      error:false,
      user: {
        email: null,
        password: null
      }
    }),
        methods: {
      ...mapActions('auth',['loginUser','logoutUser']),

      async login() {
        console.log("entro al login ")
        await this.loginUser(this.user)
          .catch(() => {
              // Handle error
              this.error=true;
            }
          );
          //Cleaning
          this.user = {
                email: null,
                password: null
              }

          if (this.isLoggedIn) {
              this.$router.push('/login')
          }
      },
      async logout() {
        await this.logoutUser().catch((err) => {
          console.log(err);
        });
        this.error=false;
        this.user = {
          email: null,
          password: null
        }
        this.$router.push('/');
      },
    }
  }



// import axios from "axios";

// const ENDPOINT_PATH = "http://127.0.0.1:5000/api/auth/login_jwt";

// export default {
//   data: () => {
//     return {
//       email: '',
//       password: '',
//     };
//   },
//   methods: {
//     login(email, password) {
//     const user = { email, password };
//     console.log(user)
//     return axios.post(ENDPOINT_PATH + "login", user);
//     // async login(){
//     //   console.log("entrooooooo")
//     //   console.log(this.email)
//     //   var payload = {
//     //     email: this.email,
//     //     password: this.password
//     //   };
//     //   console.log(payload)
//     // }
//   },
// },
//}
</script> 


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