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
from src.web.controllers.api.club import disciplines
from src.web.controllers.api.me import disciplinas
from src.web.controllers.api.me import profile
from src.web.controllers.api.me import pagos_de_un_asociado
from src.web.controllers import asociado_controller
from src.web.controllers import config_controller


from src.web.controllers import cuota_controller

# Imports tablas de los modelos
from src.core.models.usuario_model import Usuario
from src.core.models.rol_model import Rol
from src.core.models.permiso_model import Permiso
from src.core.models.asociado_model import Asociado
from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota
from src.core.models.config_model import Config
from src.core.models.pago_model import Pago

from src.web.helpers.permiso import validar_permisos, es_admin
from src.web.helpers import handlers
from src.core.config import config
from src.core import seeds
from src.core import database
from src.core import seeds 
from src.core.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_session.__init__ import Session
from os import error
from flask_cors import CORS
# from routes import auth


# def create_app(static_folder="static"):
def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])
    CORS(app)
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
    app.add_url_rule('/registrar_usuario', 'register_user', usuarios_controller.register_validation, methods=["GET", "POST"])
    app.add_url_rule("/gestion_usuarios/bhuscar", "buscar_usuario", usuarios_controller.buscar_usuario, methods=["GET"])

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
    app.add_url_rule('/ver_perfil', 'ver_perfil',index_controller.ver_perfil, methods=['POST', 'GET'])
    app.add_url_rule('/ver_disciplinas', 'ver_disciplinas', index_controller.ver_disciplinas) 
    app.add_url_rule('/ver_cuotas_pagas', 'ver_cuotas_pagas', index_controller.ver_cuotas_pagas)

    #Configuracion
    app.add_url_rule("/configuracion", "config_update", config_controller.update, methods=["POST"])
    
    #Operaciones Usuarios
    app.add_url_rule('/crear_usuario', 'crear_usuario', usuarios_controller.crear_usuario, methods=["POST", "GET"])
    app.add_url_rule('/eliminar_usuario/<id>', 'eliminar_usuario', usuarios_controller.eliminar_usuario)
    app.add_url_rule('/modificar_usuario/<id>', 'modificar_usuario', usuarios_controller.modificar_usuario, methods=["POST", "GET"])
    app.add_url_rule('/activar_desactivar/<id>', 'activar_desactivar', usuarios_controller.activar_desactivar)
    app.add_url_rule('/agregar_rol/<id>', 'agregar_rol', usuarios_controller.agregar_rol , methods=["POST", "GET"])
    app.add_url_rule('/eliminar_rol/<id>', 'eliminar_rol', usuarios_controller.eliminar_rol, methods=["POST", "GET"])
    
    #Operaciones Disciplina
    app.add_url_rule('/crear_disciplina', 'crear_disciplina', disciplina_controller.crear_disciplina, methods=["POST", "GET"])
    app.add_url_rule('/eliminar_disciplina/<id>', 'eliminar_disciplina', disciplina_controller.eliminar_disciplina)
    app.add_url_rule('/modificar_disciplina/<id>', 'modificar_disciplina', disciplina_controller.modificar_disciplina, methods=["POST", "GET"])
    app.add_url_rule('/habilitar_deshabilitarDisc/<id>', 'habilitar_deshabilitarD', disciplina_controller.habilitar_deshabilitar)
    
    #Operaciones Asociados
    app.add_url_rule('/crear_asociado', 'crear_asociado', asociado_controller.crear_asociado, methods=["POST", "GET"])
    app.add_url_rule('/eliminar_asociado/<id>', 'eliminar_asociado', asociado_controller.eliminar_asociado)
    app.add_url_rule('/modificar_asociado/<id>', 'modificar_asociado', asociado_controller.modificar_asociado, methods=["POST", "GET"])
    app.add_url_rule('/inscribir_asociado_disciplina/<id>', 'inscribir_asociado_disciplina', asociado_controller.inscribir_asociado_disciplina)
    app.add_url_rule('/realizar_inscripcion/<id_a> <id_d>', 'realizar_inscripcion', asociado_controller.realizar_inscripcion)  
    app.add_url_rule('/habilitar_deshabilitarAsoc/<id>', 'habilitar_deshabilitarA', asociado_controller.habilitar_deshabilitar)
    app.add_url_rule('/export_pdf', 'export_pdf', asociado_controller.export_pdf)
    app.add_url_rule('/export_csv', 'export_csv', asociado_controller.export_csv) 
    app.add_url_rule("/bhuscar_usaurio", "buscar_usuario_asociado", asociado_controller.buscar_usuario_asociado, methods=["GET"])
    
    
    #Operaciones Couta
    app.add_url_rule('/realizar_pago/<id_a><id_d>', 'realizar_pago', cuota_controller.realizar_pago, methods=["POST", "GET"])
    app.add_url_rule('/pagar_cuota/<id_c> <monto><id_d> <id_a> ', 'pagar_cuota', cuota_controller.pagar_cuota)
    app.add_url_rule('/ver_recibo_cuota<cuota_id>', 'ver_recibo_cuota', cuota_controller.ver_recibo_cuota)
    #manejo de errores
    app.register_error_handler(404, handlers.not_found_error)
    app.register_error_handler(401, handlers.not_authorize)
    #agregar error 403

    
    #datos roles y permisos
    
    # Endpoints para la api de disciplinas 
    app.add_url_rule('/api/club/discipline/<int:id>', 'mostrar_disciplina',disciplines.mostrar_disciplina, methods=['GET'])
    app.add_url_rule('/api/club/disciplines', 'mostrar_disciplinas',disciplines.mostrar_disciplinas, methods=['GET'])

     # Endpoints para la api de usuario
    app.add_url_rule('/api/me/discipline/<int:id>', 'mostrar_disciplinas_de_un_asociado', disciplinas.mostrar_disciplinas_de_un_asociado, methods=['GET'])
    app.add_url_rule('/api/me/profile/<int:id>', 'mostrar_usuario', profile.mostrar_usuario, methods=['GET'])
    app.add_url_rule('/api/me/payments/<int:id>', 'mostrar_pagos_de_un_asociado', pagos_de_un_asociado.mostrar_pagos_de_un_asociado, methods=['GET'])
    app.add_url_rule('/api/me/payments/cuota/<int:id>', 'cargar_pago', pagos_de_un_asociado.cargar_pago, methods=["POST", "GET"])


    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()

    @app.cli.command(name="seeds")
    def seedsdb():
        seeds.run()

    @app.shell_context_processor
    def make_shell_context():
        modules = dict(app=app)
        
        modelsmodule = importlib.import_module('src.core.models')
        # import ipdb
        # ipdb.set_trace() #breakpoint
        for modulename in modelsmodule.__dict__:
            modules[modulename] = getattr(modelsmodule, modulename)
        return modules 
    app.jinja_env.globals.update(validar_permisos=validar_permisos)
    app.jinja_env.globals.update(es_admin=es_admin)
    return app