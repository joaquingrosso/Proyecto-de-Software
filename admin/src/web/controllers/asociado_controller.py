
from unicodedata import category
from src.core.models.asociado_model import Asociado
from flask import render_template ,request, redirect, url_for ,flash 

def register_database(first_name, last_name, document_type, document, gender, member_number, adress, state ,phone_number , email):
    asociado = Asociado(first_name, last_name, document_type, document, gender, member_number, adress, state ,phone_number , email)
    asociado.register_asociado_database()        
    return redirect(url_for("gestion_asociados"))  

def crear_asociado():
    if request.method == 'POST':
        valido = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                valido = False
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        document_type = request.form.get('document_type')
        document = request.form.get('document')
        gender = request.form.get('gender')
        member_number = request.form.get('member_number')
        adress = request.form.get('address')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        state = request.form.get('state')
        #if not verify_disciplina(name, category) and valido: #se chequea que el usuario no exista y que no tenca campos vacios
        register_database(first_name, last_name, document_type, document, gender, member_number, adress, state ,phone_number , email)
        return redirect(url_for("gestion_asociados"))  
    return render_template('asociado/crear_asociado.html')

def eliminar_asociado():
    return redirect(url_for("gestion_asociados"))

def modificar_asociado(id):
    
    asoc = Asociado.get_asociado_by_id(id)
    if request.method == "POST":
        valido = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                valido = False
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        document_type = request.form.get('document_type')
        document = request.form.get('document')
        gender = request.form.get('gender')
        member_number = request.form.get('member_number')
        adress = request.form.get('address')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')

        #validaciones de modificar
       
        if valido:
          asoc.update_asociado_database(first_name, last_name, document_type, document, gender, member_number, adress ,phone_number , email)
          return redirect(url_for("gestion_asociados")) 
        # return render_template('/user/modificar_usuario.html', usu=usu) 
        return redirect(url_for("gestion_asociados"))  