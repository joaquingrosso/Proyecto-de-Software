from unittest import result
from flask import jsonify
from flask import request
from src.core.models.pago_model import Pago
from src.core.models.asociado_model import Asociado
from src.core.models.cuota_model import Cuota
from src.core.models.config_model import Config
from datetime import datetime
from src.web.controllers import cuota_controller
from src.web.controllers.api.auth.login_jwt import token_required

@token_required
def mostrar_pagos_de_un_asociado(current_user):
   try:
        lista = []
        asociado_actual = Asociado.query.get(current_user.asociado_id)
        cuotas = Cuota.cuota_asociado(current_user.asociado_id)
        print(asociado_actual)
        print(cuotas)
        for cuota in cuotas:
          #pago_cuota = Pago.pago_asociado(cuota.id)
          #if pago_cuota is not None:
          c = {   
                    "periodo" : cuota.periodo, 
                    #"estado":   cuota.estado, 
                    "monto": cuota.monto                                                 
               }
          lista.append(c)
   except:
        return jsonify({"error": "500 Internal server Error"}), 500
    
   if not asociado_actual:
     return jsonify({"error": "404 el id no existe"}), 404
#    dic= { 

#             "id" : asociado_actual.id,
#             "nombre del Asociado": asociado_actual.first_name,
#            }
    
#   resp= {'datos del asociado':dic, 'pagos': lista }
   resp= lista
   return jsonify(resp), 200


#pago de un asociado
def cargar_pago(id):
     cuota_actual = Cuota.query.get(id)
     cuota_actual = Cuota.get_cuota_by_id(id)
     print(cuota_actual)
     try:
          if cuota_actual is None:
               return jsonify({"error": "404 la cuota no existe"}), 404
          if request.method == "POST" :
               if Pago.pago_de_una_cuota(cuota_actual.id) is None:
                    monto = request.json['monto']
                    periodo = request.json['periodo']
                    cuota_actual.estado = Cuota.get_estado_paga()
                    fecha_hoy = datetime.now()
                    recargo_cuota = Config.get_valor_porcentaje()
                    dia_actual=int(fecha_hoy.strftime('%d'))
                    mes_actual=int(fecha_hoy.strftime('%m'))
                    if dia_actual >= 1 and dia_actual <= 10:
                         cuota_actual.register_cuota_database()
                         cuota_controller.register_pago_database(id, monto, periodo)
                    else:
                         recargo = (cuota_actual.monto * recargo_cuota)/100
                         monto_recargo = cuota_actual.monto + recargo
                         cuota_actual.monto = monto_recargo
                         cuota_actual.register_cuota_database()
                         cuota_controller.register_pago_database(id, monto_recargo, cuota_actual.periodo)
               else: 
                    return "la cuota ya fue pagada"
          return "pago la cuota con exito"
     except:
          return jsonify({"error": " al cargar datos"}), 404
     