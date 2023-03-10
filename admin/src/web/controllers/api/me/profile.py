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

   if asociado is not None:
      dic = {
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
       dic = {
            "user": current_user.username,
            "email": current_user.email,
            "number": "",
            "document_type": "",
            "document_number": "",
            "gender": "",
            "address": "",
            "phone": ""
         }
   resp = dic
   return jsonify(resp), 200


# carnet digital
@token_required
def carnet_digital(current_user):
#    import pdb
#    pdb.set_trace()
   if not current_user:
        return jsonify({"error": "404"}), 404
   asociado = Asociado.get_asociado_by_id(current_user.asociado_id)
   cuotas_pagas = Cuota.cuota_asociado(current_user.asociado_id)
   fecha = asociado.get_fecha()
   dia_actual=fecha.strftime('%d')
   mes_actual=fecha.strftime('%m')
   año_actual=fecha.strftime('%Y')
   fecha_ingreso= dia_actual+ "/" + mes_actual +"/"  + año_actual
   if asociado is not None and cuotas_pagas is not None:
      dic= { 
            "status": "OK",
            "description": Cuota.validar_deuda_cuota(cuotas_pagas),
            "profile": {
               "user": current_user.username,
               "email": current_user.email,
               "number": asociado.id,
               "first_name": asociado.first_name,
               "last_name": asociado.last_name,
               "document_type": asociado.document_type,
               "document_number": asociado.document,
               "gender": asociado.gender,
               "address": asociado.adress,
               "phone":asociado.phone_number,
               "fecha_alta":fecha_ingreso
            }
           
         }
   else:
      return jsonify({"error": "404"}), 404
   resp= dic 
   return jsonify(resp), 200
   