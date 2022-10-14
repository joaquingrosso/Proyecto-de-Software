from unicodedata import category
from src.core.models.disciplina_model import Disciplina
from flask import render_template ,request, redirect, url_for ,flash 



def register_database(name, category, instructors, date_time, monthly_cost, enabled=True):
    
    disciplina = Disciplina(name, category, instructors, date_time, monthly_cost, enabled)
    disciplina.register_disciplina_database()
        
    return redirect(url_for("gestion_disciplinas"))  

def crear_disciplina():
    if request.method == 'POST':
        valido = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                valido = False
        name = request.form['name']
        category = request.form['category']
        instructors = request.form['instructors']
        date_time = request.form['date_time']
        monthly_cost = request.form['monthly_cost']
        #if not verify_disciplina(name, category) and valido: #se chequea que el usuario no exista y que no tenca campos vacios
        register_database(name, category, instructors, date_time, monthly_cost)
        return redirect(url_for("gestion_disciplinas"))  
    return render_template('disciplina/crear_disciplina.html')

def eliminar_disciplina():
    return redirect(url_for("gestion_disciplinas"))

def modificar_disciplina(id):
    
    disip = Disciplina.get_disciplina_by_id(id)
    if request.method == "POST":
        valido = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                valido = False
        name = request.form['name']
        category = request.form['category']
        instructors = request.form['instructors']
        date_time = request.form['date_time']
        monthly_cost = request.form['monthly_cost']

        #validaciones de modificar
       
        if valido:
          disip.update_disciplina_database(name, category, instructors, date_time, monthly_cost)
          return redirect(url_for("gestion_disciplinas")) 
        # return render_template('/user/modificar_usuario.html', usu=usu) 
        return redirect(url_for("gestion_disciplinas"))  
    
