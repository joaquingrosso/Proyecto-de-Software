from unittest import result
from flask import jsonify
from flask import request
from src.core.models.pago_model import Pago
from src.core.models.asociado_model import Asociado
from src.core.models.cuota_model import Cuota

def mostrar_pagos_de_un_asociado(id):
   try:
        lista = []
        asociado_actual = Asociado.query.get(id)
        cuotas = Cuota.cuota_asociado(id)
        for cuota in cuotas:
          pago_cuota = Pago.pago_asociado(cuota.id)
          if pago_cuota is not None:
               c = {   
                         "periodo" : cuota.periodo, 
                         "estado":   cuota.estado, 
                         "monto": pago_cuota.monto                                                 
                    }
               lista.append(c)
   except:
        return jsonify({"error": "500 Internal server Error"}), 500
    
   if not asociado_actual:
        return jsonify({"error": "404 el id no existe"}), 404
   dic= { 

            "id" : asociado_actual.id,
            "nombre del Asociado": asociado_actual.first_name,
           }
    
   resp= {'datos del asociado':dic, 'pagos': lista }
   return jsonify(resp), 200


#pago de un asociado
def cargar_pago(id):
     cuota_actual = Cuota.query.get(id)
     cuota_actual = Cuota.get_cuota_by_id(id)
     # asociado_actual = Asociado.get_asociado_by_id(cuota_actual.asociado_id) 
     # print(asociado_actual) 
     try:
          if not cuota_actual:
               return jsonify({"error": "404 el id no existe"}), 404
          if request.method == "POST" :
               monto = request.json['monto']
               periodo = request.json['periodo'] 
               # print(monto)
               # print(periodo)     
               pago = Pago.pago_de_una_cuota(id)
               # print(pago)
               pago.actualizar_pago(monto,periodo)
          # return jsonify(request), 201 
          return "pago la cuota con exito"
     except:
          return jsonify({"error": " al cargar datos"}), 404
     