from flask import redirect, render_template, request, url_for, session, flash
from src.core.models.usuario_model import Usuario
from src.core.models.disciplina_model import Disciplina
from src.core.models.asociado_model import Asociado

from functools import wraps
from src.web.controllers import login_required

@login_required
def inicio():
    return render_template("inicio_privada.html") 


@login_required
def gestion_usuarios(nombre=' ' ):
    usuariosActualesActivos = Usuario.list_usuarios()
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_usuarios.html", user=usuariosActualesActivos ) 

@login_required
def gestion_asociados(nombre=' ' ):
    asociadosActuales = Asociado.list_asociados()
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_asociados.html", asoc = asociadosActuales)

@login_required
def gestion_disciplinas(nombre=' '):
    disciplinasActualesActivas = Disciplina.list_disciplina()  
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_disciplinas.html", discip = disciplinasActualesActivas)

@login_required
def pago_cuotas():
    lista_asociados = Asociado.list_asociados()
    return render_template("pago_cuotas.html", listaA = lista_asociados )

@login_required
def configuracion():
    return render_template("configuracion.html")

@login_required
def ver_perfil():
    username = session['username']
    user = Usuario.query.filter_by(username=username).first()
    return render_template('user/ver_perfil.html', user=user)