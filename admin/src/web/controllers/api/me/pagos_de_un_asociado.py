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
import json


@token_required
def mostrar_pagos_de_un_asociado(current_user):
    try:
        dic_mes = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
                   "Julio": 7, "Agosto": 8, "Septembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12}
        lista = []
        asociado_actual = Asociado.query.get(current_user.asociado_id)
        cuotas = Cuota.cuota_asociado(current_user.asociado_id)
        fecha_hoy = datetime.now()
        recargo_cuota = Config.get_valor_porcentaje()
        dia_actual = int(fecha_hoy.strftime('%d'))
        mes_actual = int(fecha_hoy.strftime('%m'))

        for cuota in cuotas:
            mes = cuota.periodo.split(" ")
            if dic_mes.get(mes[0]) > mes_actual or cuota.estado == "Paga":
                c = {
                    "periodo": cuota.periodo,
                    "estado": cuota.estado,
                    "monto": cuota.monto
                }
                lista.append(c)
            else:
                if dia_actual >= 1 and dia_actual <= 10:
                    c = {
                        "periodo": cuota.periodo,
                        "estado":   cuota.estado,
                        "monto": cuota.monto
                    }
                    lista.append(c)
                else:
                    recargo = (cuota.monto * recargo_cuota)/100
                    c = {
                        "periodo": cuota.periodo,
                        "estado":   cuota.estado,
                        "monto": cuota.monto + recargo
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
    resp = lista
    return jsonify(resp), 200


# pago de un asociado
@token_required
def cargar_pago(current_user):
    cuota_actual = Cuota.query.get(current_user.asociado_id)
    recargo_cuota = Config.get_valor_porcentaje()
    try:
        if request.method == "POST":
            pagos = json.loads(request.data)
            monto = pagos.get('monto')
            periodo = pagos.get('periodo')
            monto_sin_recargo = (monto * 100)/(100 + recargo_cuota)
            cuota = Cuota.query.filter_by(
                asociado_id=current_user.asociado_id, periodo=periodo, monto=monto_sin_recargo).first()
            if cuota is None:
                return jsonify({"error": "404 la cuota no existe"}), 404
            if Pago.pago_de_una_cuota(cuota.id) is None:
                cuota.estado = Cuota.get_estado_paga()
                fecha_hoy = datetime.now()
                recargo_cuota = Config.get_valor_porcentaje()
                dia_actual = int(fecha_hoy.strftime('%d'))
                mes_actual = int(fecha_hoy.strftime('%m'))
                if dia_actual >= 1 and dia_actual <= 10:
                    cuota.register_cuota_database()
                    pago = Pago(cuota.id, monto_sin_recargo,periodo)
                    pago.register_pago_database()
                else:
                    recargo = (cuota.monto * recargo_cuota)/100
                    monto_recargo = cuota.monto + recargo
                    cuota.monto = monto_recargo
                    cuota.register_cuota_database()
                    pago = Pago(cuota.id, monto_recargo,cuota.periodo)
                    pago.register_pago_database()
            else:
                return "la cuota ya fue pagada"
        return "pago la cuota con exito"
    except:
        return jsonify({"error": " al cargar datos"}), 404
