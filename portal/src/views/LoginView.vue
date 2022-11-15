
 <template>

  
  <div class="conteiner">
    <form @submit.prevent="login" >

      <div class="imge"><img src="../../public/img/logo2.png"></div>

      <h1 class="h3 mb-3 fw-normal">Inicio Sesion</h1>

      <input v-model="email" type="email" class="form-control" placeholder="Email" required>

      <input v-model="password"  type="password" class="form-control" placeholder="Password" required>

      <button class="w-100 btn btn-lg btn-primary" type="submit">Iniciar sesion</button>
    </form>
  </div>
    
</template> 

<script>

import axios from "axios";
const path = "http://127.0.0.1:5000/api/auth";
// var axios = require("axios");

// const axiosInstance = axios.create({
//   headers: {
    
//   }
// });
export default {
  data: () => ({
    email: "",
    password: ""
  }),
  methods: {
    login() {
      console.log(this.email);
      console.log(this.password);
      // this.$router.push({name:'disciplinas'})
      axios.post(path,{email: this.email,password:this.password},{headers:{"Access-Control-Allow-Origin": "*"}}).then((response) => {
        console.log(response.data)
        console.log(response.status)
        console.log("ok")
       }).catch((data) => {
        console.log(data)
        console.log("error")
       })
    }
    
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