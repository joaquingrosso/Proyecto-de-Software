from flask import Flask
from flask import render_template


def not_found_error(e):
     kwargs = {
         "error_name": "404 not found error",
         "error_description": "La url a la que quiere acceder no existe", 
     }
     return render_template("error.html", **kwargs), 404


def not_authorize(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No está autorizado para acceder a la url",
    }
    return render_template("error.html", **kwargs), 401