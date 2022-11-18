from flask import jsonify
from src.web.controllers.api.auth.login_jwt import token_required
from src.core.models.cuota_model import Cuota
from src.core.models.asociado_model import Asociado

@token_required
def mostrar_usuario(current_user):
#    import pdb
#    pdb.set_trace()
   if not current_user:
        return jsonify({"error": "404 el id no existe"}), 404
   asociado = Asociado.get_asociado_by_id(current_user.asociado_id)
   # print(current_user)
   # print(asociado)
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


#carnet digital
@token_required
def carnet_digital(current_user):
#    import pdb
#    pdb.set_trace()
   if not current_user:
        return jsonify({"error": "404"}), 404
   asociado = Asociado.get_asociado_by_id(current_user.asociado_id)
   cuotas_pagas = Cuota.cuota_asociado(current_user.asociado_id)
   # print(cuotas_pagas)
   # print(current_user)
   # print(asociado)
   for cuota in cuotas_pagas:
           c = {    
                      "estado":   cuota.estado,                                                
               }
   if asociado is not None:
      dic= { 
            "nombre": current_user.first_name,
            "apellido": current_user.last_name,
            "numero_socio": asociado.id,
            "document_type": asociado.document_type,
            "document_number": asociado.document,
            "fecha_de_alta": asociado.phone_number,
            "estado":   cuota.estado
            #"estado":   cuotas_pagas.validar_periodo_actual()
         }
   resp= dic 
   return jsonify(resp), 200
   