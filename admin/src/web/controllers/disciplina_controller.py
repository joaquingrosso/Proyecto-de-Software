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
    return render_template('/user/modificar_usuario.html', disip=disip)   

# def crear_usuario():
#     if request.method == 'POST':
#         valido = True
#         for clave,valor in request.form.items():
#             if valor == '':
#                 msg_error = f"El campo {clave} esta vacio"
#                 flash(msg_error)
#                 valido = False
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         email = request.form['email']
#         password = request.form['password']
#         username = request.form['username']
#         if not verify_user(username, email) and valido: #se chequea que el usuario no exista y que no tenca campos vacios
#             register_database(email, username, password, first_name, last_name)
#             return redirect(url_for("gestion_usuarios"))  
#     return render_template('user/crear_usuario.html')


    
# def eliminar_usuario(id):
#     usu = Usuario.get_user_by_id(id)
#     usu.delete()
#     return redirect(url_for("gestion_usuarios"))

# def modificar_usuario(id):
#     usu = Usuario.get_user_by_id(id)
#     if request.method == "POST":
#         valido = True
#         for clave,valor in request.form.items():
#             if valor == '':
#                 msg_error = f"El campo {clave} esta vacio"
#                 flash(msg_error)
#                 valido = False
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         email = request.form['email']
#         username = request.form['username']
            
#         if usu.username != username:
#             if verify_username(username):
#                 valido = False

#         if usu.email != email:
#             if verify_email(email):
#                 valido = False
       
#         if valido:
#           usu.update_user_database(first_name,last_name,email,username)
#           return redirect(url_for("gestion_usuarios"))      
#     return render_template('/user/modificar_usuario.html', usu=usu)   