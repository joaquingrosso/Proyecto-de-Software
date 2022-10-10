from flask import redirect, render_template, request, url_for, session, flash
from src.core.models.usuario_model import Usuario

def inicio():
    return render_template("inicio_privada.html") 

def gestion_usuarios(nombre=' ' ):
    usuariosActualesActivos = Usuario.list_usuarios()
    print(usuariosActualesActivos)
    if request.method == 'GET':
        nombre = nombre
    return render_template("gestion_usuarios.html", user=usuariosActualesActivos) 

def gestion_asociados():
    return render_template("gestion_asociados.html")

def gestion_disciplinas():
    return render_template("gestion_disciplinas.html")

def pago_cuotas():
    return render_template("pago_cuotas.html")

def configuracion():
    return render_template("configuracion.html")