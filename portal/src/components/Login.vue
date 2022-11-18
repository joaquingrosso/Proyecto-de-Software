

 <template>

  <div class="conteiner">

    <form action class="form" @submit.prevent="login">
      <div class="imge"><img src="../../public/img/logo2.png"></div>
  
      <input v-model="user.email" placeholder="Email" class="form-control" type="email" id="email" required>
      
      <input v-model="user.password" placeholder="Password" type="password" autocomplete="on" class="form-control" id="password" required>
      <p v-if="error" class="error">Has introducido mal el email o la contraseña.</p>
      <input class="w-100 btn btn-lg btn-primary" type="submit" value="Login">
    </form>
  </div>
    
</template> 

<script>

import { mapActions , mapGetters } from 'vuex'

export default {
  data: () => ({
    error:false,
    user: {
      email: null,
      password: null
    }
  }),
  computed: {
      ...mapGetters({
        authUser: 'auth/user',
        isLoggedIn: 'auth/isLoggedIn'
      })
    },
  methods: {
    ...mapActions('auth',['loginUser','logoutUser']),
    async login() {
      await this.loginUser(this.user)
          .catch(() => {
              // Handle error
              this.error = true;
            }
          );
          //Cleaning
          this.user = {
                email: null,
                password: null
              }
          if (this.isLoggedIn) {
            this.$router.push('/')
          }
    },
    
    
  }
};
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