from logging import handlers
from flask import Flask
from flask import render_template, request, redirect , url_for, flash, session
from src.web.controllers import auth_controller
from src.core.models.usuario_model import Usuario
from src.web.helpers import handlers
from src.core.config import config
from src.core import database
from src.core.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_session.__init__ import Session
from os import error
# from routes import auth

# def create_app(static_folder="static"):
def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    # configuracion de la bd
    database.init_app(app)
    app.secret_key= "holamundo"
    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    
# #ruta al login 
    @app.route("/")
    def home():
<<<<<<< HEAD
        return redirect(url_for("login"))
    
    #ruta al login
    @app.route("/login", methods=["GET" , "POST"])
    def login():
        if request.method == "POST":
            print(request.form['username'])
            print(request.form['password'])
            username = request.form['username']
            password = request.form['password']
            session["username"] = username
            session["password"] = password
            user = Usuario.query.filter_by(username=username).first()
            print(user)
            if user:
                 if user.password == password:
                    return redirect(url_for("prueba_usuario", user=user.username))
                 elif user.password != password:
                     flash("el nombre de usuario o contraseña es incorrecto")
            else:
                 flash("el nombre de usuario o contraseña es incorrecto")
                 return redirect(url_for("login"))
    
        return render_template("auth/login.html")               

    @app.route("/loguot")
    def logout():
            session.pop("username", None)
            print("logout")
            return redirect(url_for("login"))


    @app.route("/prueba_usuario/")
    def prueba_usuario():
            
            return render_template("prueba_usuario.html") 
    
=======
        return redirect(url_for('login'))
           
    # Autenticacion
    app.add_url_rule('/iniciar_sesion', 'login', auth_controller.login, methods=["GET", "POST"])
    app.add_url_rule('/cerrar_sesion', 'logout', auth_controller.logout)

    #manejo de errores
>>>>>>> 4bc8b882d15a84dc7254cb2ff394791978181fa2
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(401, handlers.not_authorize)

    # @app.cli.command(name="resetdb")
    # def resetdb():
    #     database.reset_db()
        
    return app