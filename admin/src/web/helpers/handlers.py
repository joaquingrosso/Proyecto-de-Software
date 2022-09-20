from flask import Flask
from flask import render_template


def not_found_error(e):
     kwargs = {
         "error_name": "404 not found error",
         "error_description": "La url a la que quiere acceder no existe", 
     }
     return render_template("error.html", **kwargs), 404



# def not_found_error(e):
#      kwargs = {
#          "error_name": "500 Internal server Error",
#          "error_description": "Error interno del servidor", 
#      }
#      return render_template("error500.html", **kwargs), 500
