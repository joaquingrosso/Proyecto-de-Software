from flask import redirect, render_template, request, url_for, session, flash
from src.core.models.usuario_model import Usuario
from src.core.models.disciplina_model import Disciplina
from src.core.models.asociado_model import Asociado
from src.core.models.config_model import Config

def inicio():
    return render_template("inicio_privada.html") 

def gestion_usuarios(nombre=' ' ):
    config = Config.get_self(Config, 1)
    page = request.args.get('page', 1, type=int)
    usuariosActualesActivos = Usuario.list_usuarios(page,config.cant)
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_usuarios.html", user=usuariosActualesActivos ) 

def gestion_asociados(nombre=' ' ):
    config = Config.get_self(Config, 1)
    page = request.args.get('page', 1, type=int)
    asociadosActuales = Asociado.list_asociados(page,config.cant)
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_asociados.html", asoc = asociadosActuales)

def gestion_disciplinas(nombre=' '):
    config = Config.get_self(Config, 1)
    page = request.args.get('page', 1, type=int)
    disciplinasActualesActivas = Disciplina.list_disciplina(page,config.cant) 
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_disciplinas.html", discip = disciplinasActualesActivas)

def pago_cuotas():
    return render_template("pago_cuotas.html")

def configuracion():

    config = Config.get_self(Config, 1)
    return render_template("configuracion.html", config=config)

def ver_perfil():
    username = session['username']
    user = Usuario.query.filter_by(username=username).first()
    return render_template('user/ver_perfil.html', user=user)