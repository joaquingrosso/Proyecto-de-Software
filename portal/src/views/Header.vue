<template>
  <main>

    <div id="cabecera" class="content">
      <div class="box_logo">
        <a href=""><img src="../../public/img/logo2.png"></a>
      </div>
      <div class="box_title">
        <h1>Club Deportivo Villa Elisa</h1>
      </div>
      <div class="box_buttons" v-if="isLogged">
        <button type="button" class="btn btn-primary" @click="logout">Cerrar Sesion</button>
      </div>
      <div class="box_buttons" v-else>
        <RouterLink to="/login"><button type="button" class="btn btn-primary">Iniciar Sesion</button></RouterLink>
      </div>
    </div>


    <!-- Menu -->
    <nav class="nav_bar">
      <div id="menu" class="nav_header">

        <ul>
          <RouterLink to="/">
            <li class="nav-item">Inicio</li>
          </RouterLink>
          <div v-if="isLogged">
            <RouterLink to="/mis_disciplinas">
            <li class="nav-item" >Mis Disciplinas</li>
            </RouterLink>
          </div>
          <div v-else>
            <RouterLink to="/disciplinas">
              <li class="nav-item">Disciplinas</li>
            </RouterLink>          
          </div>
          <RouterLink to="/contacto">
            <li class="nav-item">Contacto</li>
          </RouterLink>
          <RouterLink to="/descripcion">
            <li class="nav-item">Descripcion</li>
          </RouterLink>
          <RouterLink to="/estadistica">
            <li class="nav-item">Estadistica</li>
          </RouterLink>
          <RouterLink to="/cuotas_pagas">
            <li class="nav-item" v-if="isLogged">Pagos Realizados</li>
          </RouterLink>
          <RouterLink to="/cuotas">
            <li class="nav-item" v-if="isLogged">Pagos Disponibles</li>
          </RouterLink>
          <RouterLink to="/carnet">
            <li class="nav-item" v-if="isLogged">Carnet</li>
          </RouterLink>
          
        </ul>

      </div>
    </nav>

  </main>
</template>

<script>
import { mapGetters , mapActions } from 'vuex'

export default {
  data () {
    return {
      isLogged: false,
      }
  },
  computed: {
      ...mapGetters({
        isLoggedIn: 'auth/isLoggedIn',
        getUser: 'auth/user'
      })
    },
  methods: {
    
    setLogged(){
      this.isLogged = this.isLoggedIn
    },
    ...mapActions('auth',['logoutUser', 'establecerStateLoggedIn_User']),
    async logout() {
        await this.logoutUser();
        localStorage.removeItem('token');
        localStorage.removeItem('isLoggedIn');
        localStorage.removeItem('user');
        this.error=false;
        this.user = {
          email: null,
          password: null
        }

        if (this.$router.currentRoute.value.fullPath == '/')  {
          this.$router.go();
        }else{
          this.$router.push('/'); 
        }
      },
    async recuperarStorage(){
      const aux = localStorage.getItem("isLoggedIn")
      if (aux != null) {
        await this.establecerStateLoggedIn_User()
      } 
    } 
    },
  
  created () {
    this.recuperarStorage()
    this.setLogged()
  }
}
</script>
<style>
#cabecera {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  position: relative;
  width: 100%;
  height: 11.5rem;
  padding: 0 1rem;
}

#carouselExampleControls {
  width: 50%;
  height: 50%;

}



.box_logo img {
  width: 75%;
}


.box_title h1 {
  font-size: 70px;
}

.box_buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 1rem;

}

.box_buttons a {
  text-decoration: none;
}

.box_buttons button {
  width: 12rem;
  text-align: center;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
}


.btn-primary {
  font-size: 25px;
}

.nav_bar {
  border-top: 5px ridge rgb(3, 2, 2);
  margin: 1rem 0;
  padding: 1.5rem 0;
}

.nav_header ul {
  list-style: none;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  gap: 2rem;
  background-color: rgba(0, 0, 0, 0.068);
  padding: 1.7rem 0;

}

.nav_header ul a {
  text-decoration: none;
  font-size: 1.5rem;
  color: rgb(255, 255, 255);
  font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  letter-spacing: 1px;
  transition: all .3s ease;
}

.nav_header li {
  border: 2px solid rgb(0, 0, 0);
  width: 12rem;
  text-align: center;
  border-radius: 10px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.842);
  cursor: pointer;
  height: 5rem;
  
}


.nav_header li:hover {
  scale: 1.05;
  transition: all .3s ease;
}

.nav_header ul a:hover {
  color: white;
  font-weight: bold;
  cursor: pointer;
  transition: all .3s ease;
}
</style>