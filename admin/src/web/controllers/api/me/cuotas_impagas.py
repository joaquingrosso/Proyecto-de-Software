from flask import jsonify
from flask import request
from src.web.controllers.api.auth.login_jwt import token_required
from src.core.models.asociado_model import Asociado
from src.core.models.cuota_model import Cuota
from src.core.models.config_model import Config
from datetime import datetime


@token_required
def mostrar_cuotas_impagas(current_user):
    try:
        dic_mes = {"Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4, "Mayo": 5, "Junio": 6,
                "Julio": 7, "Agosto": 8, "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12}
        total=0
        asociado_actual = Asociado.query.get(current_user.asociado_id)
        fecha_hoy = datetime.now()
        recargo_cuota = Config.get_valor_porcentaje()
        dia_actual = int(fecha_hoy.strftime('%d'))
        mes_actual = int(fecha_hoy.strftime('%m'))
        dic = {
            "monto_base": Config.get_valor_cuota(),
            "disciplinas": [],
            "total_a_pagar": None
        }
        index = 0
        if asociado_actual is None:
            return jsonify({"error": "404 el Asociado no existe"}), 404
        for d in asociado_actual.disciplinas:
            disciplina = {
                "nombre": d.name,
                "cuotas": []
            }
            dic["disciplinas"].append(disciplina)
            cuota = Cuota.get_cuotas_by_disciplina_asociado(
                d.id, asociado_actual.id)
            for c in cuota:
                if c.estado == "No-Paga":
                    mes = c.periodo.split(" ")
                    if dic_mes.get(mes[0]) <= mes_actual:
                        if dia_actual >= 1 and dia_actual <= 10:
                            cuota = {
                                "periodo": c.periodo,
                                "monto": c.monto,
                                "estado":c.estado,
                            }
                            total+= c.monto
                        else:
                            recargo = (c.monto * recargo_cuota)/100
                            cuota = {
                                "periodo": c.periodo,
                                "monto": c.monto + recargo,
                                "estado":c.estado,
                            }
                            total+= c.monto + recargo
                        dic["disciplinas"][index]["cuotas"].append(cuota)
            index += 1
        dic["total_a_pagar"]= total + dic["monto_base"]

    except:
        return jsonify({"error": "500 Internal server Error"}), 500

    resp = dic
    return jsonify(resp), 200
