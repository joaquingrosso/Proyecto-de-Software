from flask import jsonify

def mostrar_info_club():
    resp ={
        "email": "clubdeportivovillaelisa@gmail.com",
        "phone": "0221 487-0193"
        }
    return jsonify(resp), 200
