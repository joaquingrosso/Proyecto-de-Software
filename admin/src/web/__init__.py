import importlib
from logging import handlers
#from admin.src.web.controllers import asociado_controller
from flask import Flask
from flask import render_template, request, redirect , url_for, flash, session

from src.web.controllers import auth_controller
from src.web.controllers import index_controller

#Controllers

from src.web.controllers import auth_controller
from src.web.controllers import usuarios_controller
from src.web.controllers import disciplina_controller
from src.web.controllers import index_controller
from src.web.controllers import api_disciplinas
from src.web.controllers import asociado_controller

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
    # permiso_admin1= Permiso("admin_index")
    # permiso_admin1.register_database()
    # permiso_admin2= Permiso("admin_new")
    # permiso_admin2.register_database()
    # permiso_admin3= Permiso("admin_destroy")
    # permiso_admin3.register_database()
    # permiso_admin4= Permiso("admin_update")
    # permiso_admin4.register_database()
    # permiso_admin5= Permiso("admin_show")
    # permiso_admin5.register_database()
    
# #ruta al login 
    @app.route("/")
    def home():
        #return redirect(url_for('login'))
         return render_template("home.html")  
    # Register user
    app.add_url_rule('/registrar_usuario', 'register_user', usuarios_controller.register_validation, methods=["GET", "POST"])
    
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
    
    #Operaciones Usuarios
    app.add_url_rule('/crear_usuario', 'crear_usuario', usuarios_controller.crear_usuario, methods=["POST", "GET"])
    app.add_url_rule('/eliminar_usuario/<id>', 'eliminar_usuario', usuarios_controller.eliminar_usuario)
    app.add_url_rule('/modificar_usuario/<id>', 'modificar_usuario', usuarios_controller.modificar_usuario, methods=["POST", "GET"])
    
    #Operaciones Disciplina
    app.add_url_rule('/crear_disciplina', 'crear_disciplina', disciplina_controller.crear_disciplina, methods=["POST", "GET"])
    app.add_url_rule('/eliminar_disciplina/<id>', 'eliminar_disciplina', disciplina_controller.eliminar_disciplina)
    app.add_url_rule('/modificar_disciplina/<id>', 'modificar_disciplina', disciplina_controller.modificar_disciplina, methods=["POST", "GET"])
    
    #Operaciones Asociados
    app.add_url_rule('/crear_asociado', 'crear_asociado', asociado_controller.crear_asociado, methods=["POST", "GET"])
    app.add_url_rule('/eliminar_asociado/<id>', 'eliminar_asociado', asociado_controller.eliminar_asociado)
    app.add_url_rule('/modificar_asociado/<id>', 'modificar_asociado', asociado_controller.modificar_asociado, methods=["POST", "GET"])

    #manejo de errores
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(401, handlers.not_authorize)
    #agregar error 403

    
    #datos roles y permisos
    
    # Endpoints para la api
    app.add_url_rule('/disciplina/<int:id>', 'mostrar_disciplina',api_disciplinas.mostrar_disciplina, methods=['GET'])
    app.add_url_rule('/disciplinas', 'mostrar_disciplinas',api_disciplinas.mostrar_disciplinas, methods=['GET'])

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


    return app