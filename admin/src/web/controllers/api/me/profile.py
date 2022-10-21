from flask import jsonify
from src.core.models.usuario_model import Usuario

def mostrar_usuario(id):
   try:
        usuario_actual = Usuario.query.get(id)
   except:
        return jsonify({"error": "500 Internal server Error"}), 500
    
   if not usuario_actual:
        return jsonify({"error": "404 el id no existe"}), 404
    
   dic= { 

            "id" : usuario_actual.id,
            "nombre de usuario": usuario_actual.username,
            "nombre" : usuario_actual.first_name,
            "apellido": usuario_actual.last_name,
            "email" : usuario_actual.email,            
         }
    
   resp= {'atributos del usuario logueado':dic }
   return jsonify(resp), 200