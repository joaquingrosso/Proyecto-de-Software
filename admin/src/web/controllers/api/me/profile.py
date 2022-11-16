from flask import jsonify
from src.web.controllers.api.auth.login_jwt import token_required
from src.core.models.usuario_model import Usuario

@token_required
def mostrar_usuario(current_user):
#    import pdb
#    pdb.set_trace()
   if not current_user:
        return jsonify({"error": "404 el id no existe"}), 404
    
   dic= { 
            # "id" : current_user.id,
            "user": current_user.username,
            "nombre" : current_user.first_name,
            "apellido": current_user.last_name,
            "email" : current_user.email,            
         }
    
   resp= dic 
   return jsonify(resp), 200