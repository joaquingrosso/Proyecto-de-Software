from flask import jsonify
from datetime import datetime

from src.core.models.asociado_model import Asociado

def asociado_por_año():
    try:
        asociados = Asociado.get_all()
        dic_mes_cant={ "January":0, "February":0, "March":0, "April":0, "May":0, "June":0,
              "July":0, "August":0, "September":0, "Octuber":0, "November":0, "December":0 }
              
        for a in asociados:
            #obtengo fecha
            fecha = a.get_fecha() 
            #corto el mes      
            mes = fecha.strftime('%B')  
            #totalizo el mes
            dic_mes_cant[mes]+=1

        resp = dic_mes_cant
        return jsonify(resp), 200

    except:
        return jsonify({"error": "500 Internal server Error"}), 500
    

def asociado_por_disciplinas():
    return none;

def morosos_al_dia():
    return none;