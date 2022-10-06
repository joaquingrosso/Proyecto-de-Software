from flask import redirect, render_template, request, url_for, session, flash

def inicio():
    return render_template("inicio_privada.html") 

def gestion_usuarios():
    return render_template("gestion_usuarios.html") 

def gestion_asociados():
    return render_template("gestion_asociados.html")

def gestion_disciplinas():
    return render_template("gestion_disciplinas.html")

def pago_cuotas():
    return render_template("pago_cuotas.html")

def configuracion():
    return render_template("configuracion.html")