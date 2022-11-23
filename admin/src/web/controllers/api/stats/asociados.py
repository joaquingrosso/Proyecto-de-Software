from flask import jsonify
from datetime import datetime

from src.core.models.asociado_model import Asociado
from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota

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
    try:
        asociados = Asociado.get_all()
        disciplinas = Disciplina.get_all()
        lista = {}
        
        for d in disciplinas:
            lista[d.name] = 0

        for a in asociados:
            disciplinas = a.disciplinas
            for d in disciplinas:
                lista[d.name]+=1              
            
        return jsonify(lista), 200
    except:
        return jsonify({"error": "500 Internal server Error"}), 500

def morosos_al_dia():
    try:
        # morosos={ "Morosos":0, "Al dia":0}
        asociados = Asociado.get_all()
        
        # fecha_hoy = datetime.now()
        # dia_actual=int(fecha_hoy.strftime('%d'))
        # mes_actual=int(fecha_hoy.strftime('%m'))

        for a in asociados:
            for d in a.disciplinas:
                cuotas = Cuota.get_cuotas_by_disciplina_asociado(d.id, a.id)                
                for c in cuotas:
                    print(a.first_name + ' ' + c.periodo.split()[0])
                #busco la cuota paga mas nueva
                
                    
        return jsonify("hola")     
    except:
        return jsonify({"error": "500 Internal server Error"}), 500

def ultimaCuotaPaga(cuotas):
    if(len(cuotas)==0):
      return None
    max = self.carList[0].price
    maxObject = self.carList[0]
    for i in self.carList:
      if(i.price>max):
        max = i.price
        maxObject = i
    return maxObject        