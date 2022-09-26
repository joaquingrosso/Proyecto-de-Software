# from flask import render_template
# from flask import request
# from flask import Blueprint

# from src.core import core

def list_usuarios():
    return core.Usuario.query.all()

# @app.get("/pruebaUsuario")
# def pruebaUsuario():
        
#     usuarios = core.list_usuarios()

#     return render_template("pruebaUsuario.html", usuarios)