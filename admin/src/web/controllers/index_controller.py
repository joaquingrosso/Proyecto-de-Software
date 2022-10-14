from flask import redirect, render_template, request, url_for, session, flash
from src.core.models.usuario_model import Usuario
from src.core.models.disciplina_model import Disciplina
from src.core.models.asociado_model import Asociado
def inicio():
    return render_template("inicio_privada.html") 

def gestion_usuarios(nombre=' ' ):
    usuariosActualesActivos = Usuario.list_usuarios()
    print(usuariosActualesActivos)
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_usuarios.html", user=usuariosActualesActivos) 

def gestion_asociados(nombre=' ' ):
    asociadosActuales = Asociado.list_asociados()
    print(asociadosActuales)
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_asociados.html", asoc = asociadosActuales)

def gestion_disciplinas(nombre=' '):
    disciplinasActualesActivas = Disciplina.list_disciplina()  
    print(disciplinasActualesActivas)
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_disciplinas.html", discip = disciplinasActualesActivas)

def pago_cuotas():
    return render_template("pago_cuotas.html")

def configuracion():
    return render_template("configuracion.html")