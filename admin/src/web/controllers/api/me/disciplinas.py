from flask import jsonify
from src.core.models.disciplina_model import Disciplina
from src.core.models.asociado_model import Asociado

def mostrar_disciplinas_de_un_asociado(id):
   try:
        asociado_actual = Asociado.query.get(id)
        disciplinas = asociado_actual.disciplinas
      #   disciplinas_del_asociado_actual = Asociado.tiene_disciplina((id))
   except:
        return jsonify({"error": "500 Internal server Error"}), 500
    
   if not asociado_actual:
        return jsonify({"error": "404 el id no existe"}), 404
   lista_disciplinas = []
   for d in disciplinas:
        disciplina = {
          "name" : d.name,
          "instructors" : d.instructors,  
          "date_time" : d.date_time
        }
        lista_disciplinas.append(disciplina)
   resp= {'disciplinas de un asociado': lista_disciplinas }
   return jsonify(resp), 200