from flask import jsonify
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
          print(pago_cuota)
          if pago_cuota is not None:
               c = {   
                         "periodo" : cuota.periodo, 
                         "estado":   cuota.estado, 
                         "monto": pago_cuota.monto                                                 
                    }
               lista.append(c)
        print(lista)
   except:
        return jsonify({"error": "500 Internal server Error"}), 500
    
   if not asociado_actual:
        return jsonify({"error": "404 el id no existe"}), 404
   dic= { 

            "id" : asociado_actual.id,
            "nombre del Asociado": asociado_actual.first_name,
            "apellido del Asociado" : asociado_actual.last_name,
           }
    
   resp= {'pagos del asociado':dic, 'pagos': lista }
   return jsonify(resp), 200