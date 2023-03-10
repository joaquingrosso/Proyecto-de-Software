from unicodedata import category
from src.core.models.disciplina_model import Disciplina
from flask import render_template ,request, redirect, url_for ,flash 
from src.web.controllers import login_required
from src.core.models.cuota_model import Cuota


@login_required
def crear_disciplina():
    if request.method == 'POST':
        vacio = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                vacio = False
        name = request.form['name']
        category = request.form['category']
        instructors = request.form['instructors']
        date_time = request.form['date_time']
        monthly_cost = request.form['monthly_cost']
        #se chequea que el usuario no exista y que no tenca campos vacios
        if vacio:
            if verify_format(monthly_cost) and not verify_disciplina(name, category) and verify_lenghts(name, category, instructors, date_time, monthly_cost): 
                register_database(name, category, instructors, date_time, monthly_cost)
                return redirect(url_for("gestion_disciplinas"))  
    return render_template('disciplina/crear_disciplina.html')

@login_required
def eliminar_disciplina(id):
    eliminar_cuota_disciplina(id)
    disci= Disciplina.get_disciplina_by_id(id)
    disci.delete()
    return redirect(url_for("gestion_disciplinas"))

@login_required
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
            if verify_format(monthly_cost) and verify_lenghts(name, category, instructors, date_time, monthly_cost) and not verify_disciplina_not_actual(id, name, category):
                disip.update_disciplina_database(name, category, instructors, date_time, monthly_cost)
                return redirect(url_for("gestion_disciplinas")) 
        # return render_template('/user/modificar_usuario.html', usu=usu) 
        return redirect(url_for("gestion_disciplinas"))  

@login_required
def habilitar_deshabilitar(id):
    disc = Disciplina.get_disciplina_by_id(id)
    if disc.enabled == Disciplina.get_disciplina_enebled():
        disc.enabled = Disciplina.get_disciplina_disabled()
    else:
        disc.enabled = Disciplina.get_disciplina_enebled()
    disc.register_disciplina_database()
    return redirect(url_for("gestion_disciplinas"))

def verify_format(monthly_cost):
    try: 
        monthly_cost = float(monthly_cost)          
    except ValueError: 
        flash("Solo puede ingresar numeros en el costo mensual")
        return False
    return  True

def verify_disciplina(nombre, category):
    disciplina = Disciplina.get_disciplina_by_name_and_category(nombre,category)
    if disciplina is not None:
        flash("La disciplina ya existe")
        return True    
    return False   

def verify_disciplina_not_actual(disc_id, name, category):
    disciplina = Disciplina.get_disciplina_by_name_and_category(name,category)   
    if disciplina is not None:
        aux = Disciplina.get_disciplina_by_id(disc_id)
        if disciplina != aux:
            flash("La disciplina ya existe")
            return True
    return False   

def verify_lenghts(name, category, instructors, date_time, monthly_cost):
    #name
    if len(name) == 0:
        flash("Nombre vacio, complete el campo")
        return False
    else:
        if len(name) > 50:
            flash("Nombre muy largo")
            return False
        elif len(name) < 5:
            flash("Nombre muy corto")
            return False   
    #category
    if len(category) == 0:
        flash("Categoria vacio, complete el campo")
        return False
    else:
        if len(category) > 50:
            flash("Categoria muy larga")
            return False
        elif len(category) < 5:
            flash("Categoria muy corta")
            return False       
    #instructors
    if len(instructors) == 0:
        flash("Instructores vacio, complete el campo")
        return False
    else:
        if len(instructors) > 50:
            flash("Instructores muy largo")
            return False
        elif len(instructors) < 5:
            flash("Instructores muy corto")
            return False   
    #date_time
    if len(date_time) == 0:
        flash("Fecha y hora vacio, complete el campo")
        return False
    else:
        if len(date_time) > 50:
            flash("Fecha y hora muy largo")
            return False
        elif len(date_time) < 5:
            flash("Fecha y hora muy corto")
            return False 
    return True

def register_database(name, category, instructors, date_time, monthly_cost, enabled=True):
    
    disciplina = Disciplina(name, category, instructors, date_time, monthly_cost, enabled)
    disciplina.register_disciplina_database()
        
    return redirect(url_for("gestion_disciplinas"))  

def eliminar_cuota_disciplina(id):
    Cuota.eliminar_disciplinas_cuota_asociado(id)
    return True