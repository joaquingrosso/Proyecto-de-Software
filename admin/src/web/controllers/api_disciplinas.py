from flask import jsonify
from src.core.models.disciplina_model import Disciplina


def mostrar_disciplina(id):
    try:
        disciplina = Disciplina.query.get(id)
    except:
        return jsonify({"error": "500 Internal server Error"}), 500
    
    if not disciplina:
        return jsonify({"error": "404 el id no existe"}), 404
    
    dic= { "id" : disciplina.id,
           "nombre": disciplina.name,
           "categoria": disciplina.category, 
         }
    
    resp= {'atributos':dic }
    return jsonify(resp), 200


#def mostrar_disciplinas(page=1):
#totalelementos=para el total
def mostrar_disciplinas():
    #disciplinas = 10
    disciplinas = Disciplina.list_disciplina()
    import ipdb
    ipdb.set_trace()
    lista = []
    for disciplina in disciplinas.items:
        dic= {  "id" : disciplina.id,
                "nombre": disciplina.name,
                "categoria": disciplina.category, 
         }
        lista.append(dic)
    resp= {'disciplinas': lista, }
    return jsonify(resp), 200

