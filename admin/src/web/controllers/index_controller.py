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
    lista_asociado = []
    lista_disciplina = []
    asociado_actual = Asociado.list_asociados()
    disciplina_actual = Disciplina.list_disciplina()
    for a in asociado_actual:
        for d in disciplina_actual:
            lista_asociado.extend(Asociado.query.filter(a.id == d.id))
            lista_disciplina.extend(Disciplina.query.filter(d.id == a.id))
    return render_template("pago_cuotas.html", listaA = lista_asociado , listaD = lista_disciplina)

def configuracion():
    return render_template("configuracion.html")