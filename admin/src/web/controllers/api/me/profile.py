from flask import jsonify
from src.web.controllers.api.auth.login_jwt import token_required
from src.core.models.usuario_model import Usuario
from src.core.models.asociado_model import Asociado

@token_required
def mostrar_usuario(current_user):
#    import pdb
#    pdb.set_trace()
   if not current_user:
        return jsonify({"error": "404 el id no existe"}), 404
   asociado = Asociado.get_asociado_by_id(current_user.asociado_id)
   print(current_user)
   print(asociado)
   if asociado is not None:
      dic= { 
            "user": current_user.username,
            "email": current_user.email,
            "number": asociado.id,
            "document_type": asociado.document_type,
            "document_number": asociado.document,
            "gender": asociado.gender,
            "address": asociado.adress,
            "phone": asociado.phone_number            
         }
   else:
       dic= { 
            "user": current_user.username,
            "email": current_user.email,
            "number": "",
            "document_type": "",
            "document_number": "",
            "gender": "",
            "address": "",
            "phone": ""           
         }
   resp= dic 
   return jsonify(resp), 200