from flask import jsonify
from src.web.controllers.api.auth.login_jwt import token_required
from src.core.models.disciplina_model import Disciplina
from src.core.models.asociado_model import Asociado

@token_required
def mostrar_disciplinas_de_un_asociado(current_user):
   
   try:
        asociado_actual = Asociado.get_asociado_by_id(current_user.asociado_id)
        if asociado_actual is None:
          return jsonify({"error": "404 el id no existe"}), 404
        disciplinas = asociado_actual.disciplinas
      #   disciplinas_del_asociado_actual = Asociado.tiene_disciplina((id))
   except:
        return jsonify({"error": "500 Internal server Error"}), 500

   lista_disciplinas = []
   for d in disciplinas:
        disciplina = {
          "name" : d.name,
          "instructors" : d.instructors,  
          "date_time" : d.date_time
        }
        lista_disciplinas.append(disciplina)
   resp= lista_disciplinas 
   return jsonify(resp), 200