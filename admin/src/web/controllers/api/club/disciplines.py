from flask import jsonify,request
from src.core.models.disciplina_model import Disciplina
from src.core.models.config_model import Config
import json

def mostrar_disciplina(id):
    try:
        disciplina = Disciplina.query.get(id)
    except:
        return jsonify({"error": "500 Internal server Error"}), 500
    
    if not disciplina:
        return jsonify({"error": "404 el id no existe"}), 404
    
    dic= { 
            "id" : disciplina.id,
            "nombre": disciplina.name,
            "instructores": disciplina.instructors,
            "dia y hora": disciplina.date_time,
         }
    
    resp= {'atributos':dic }
    return jsonify(resp), 200


def mostrar_disciplinas():
    disciplinas = Disciplina.list_disciplina()
    lista = []
    for disciplina in disciplinas:
        dic= { 
              "id" : disciplina.id,
              "nombre": disciplina.name,
              "dia_y_hora": disciplina.date_time,
              "instructores": disciplina.instructors
             }
        lista.append(dic)
    #resp= {'disciplinas': lista, 'pagina': page, 'total de disciplinas': config.cant }
    resp= lista
    return jsonify(resp), 200

