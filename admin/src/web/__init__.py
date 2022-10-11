import importlib
from logging import handlers
from flask import Flask
from flask import render_template, request, redirect , url_for, flash, session
from src.web.controllers import auth_controller
from src.web.controllers import index_controller

#Controllers

from src.web.controllers import auth_controller
from src.web.controllers import usuarios_controller

# Imports tablas de los modelos
from src.core.models.usuario_model import Usuario
from src.core.models.rol_model import Rol
from src.core.models.permiso_model import Permiso
from src.core.models.asociado_model import Asociado
from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota

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
        #return redirect(url_for('login'))
         return render_template("home.html")  
    # Register user
    app.add_url_rule('/registrar_usuario', 'register_user', usuarios_controller.register, methods=["GET", "POST"])
    
    # Autenticacion
    app.add_url_rule('/iniciar_sesion', 'login', auth_controller.login, methods=["GET", "POST"])
    app.add_url_rule('/cerrar_sesion', 'logout', auth_controller.logout)
    
    # Manejo de menu index
    app.add_url_rule('/inicio', 'inicio', index_controller.inicio)
    app.add_url_rule('/gestion_usuarios/usuarios', 'gestion_usuarios', index_controller.gestion_usuarios , methods=["GET", "POST"])
    app.add_url_rule('/gestion_asociados', 'gestion_asociados', index_controller.gestion_asociados)
    app.add_url_rule('/gestion_disciplinas', 'gestion_disciplinas', index_controller.gestion_disciplinas) 
    app.add_url_rule('/pago_cuotas', 'pago_cuotas', index_controller.pago_cuotas) 
    app.add_url_rule('/configuracion', 'configuracion', index_controller.configuracion)
    #Crear Usuario
    app.add_url_rule('/crear_usuario', 'crear_usuario', usuarios_controller.crear_usuario, methods=["POST", "GET"])
    app.add_url_rule('/eliminar_usuario/<id>', 'eliminar_usuario', usuarios_controller.eliminar_usuario)

    #manejo de errores
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(401, handlers.not_authorize)
    #agregar error 403

    
    

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.shell_context_processor
    def make_shell_context():
        modules = dict(app=app)
        
        modelsmodule = importlib.import_module('src.core.models')
        # import ipdb
        # ipdb.set_trace() #breakpoint
        for modulename in modelsmodule.__dict__:
            modules[modulename] = getattr(modelsmodule, modulename)
            
        print('Auto imported ', [i[0] for i in modules.items()])
        return modules 

    @app.route("/index")
    def index():
        #return redirect(url_for('login'))
         return render_template("index.html")  
    

    @app.route("/pruebaUsuario")
    def pruebaUsuario():
        #return redirect(url_for('login'))
        return render_template("prueba_usuario.html")  
    


    return app