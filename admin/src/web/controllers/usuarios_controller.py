from src.core.models.usuario_model import Usuario
from flask import render_template ,request , flash
from werkzeug.security import generate_password_hash , check_password_hash


def register_validation():

    if request.method == 'POST':
        valido = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                valido = False
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        if not verify_user(username, email) and valido: #se chequea que el usuario no exista y que no tenca campos vacios
            register_database(email, username, password, first_name, last_name)
    return render_template('user/register_user.html')

def verify_user(username,email):
    usuario = Usuario.query.filter_by(username=username).first()
    email = Usuario.query.filter_by(email = email).first()
    if usuario is not None:
        flash("El usuario ingresado ya existe")
        return True
    elif email is not None:
        flash("El email ingresado ya existe")
        return True
    return False

def register_database(email,username,password, first_name,last_name):
    passwd_hash = generate_password_hash(password)
    passwd1= passwd_hash[:len(passwd_hash)//2]
    passwd2= passwd_hash[len(passwd_hash)//2:]
    user= Usuario(email,username, passwd1,passwd2, first_name, last_name)
    user.register_user_database()
        user= Usuario(email,username, password, first_name, last_name)
        user.register_user_database()
        
    return render_template('user/register_user.html')


# def crear_usuario():
#     mensaje = ''
#     if request.method == 'POST':
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         email = request.form['email']
#         password = request.form['password']
#         username = request.form['username']
#         if Usuario.existe_usuario(request.form['username']):
#             mensaje="El nombre de usuario ya existe"
#         else:
#             res= user= Usuario(email,username, password, first_name, last_name)
#             if res:
#                 mensaje = "Usuario creado exitosamente"
#                 user.register_user_database()
#             else:
#                 mensaje = "Hubo algun problema"
#             return render_template('/gestion_usuarios.html', mensaje= mensaje)
#         return render_template('user/crear_usuario.html', mensaje= mensaje)
#     else:
#         return render_template('user/crear_usuario.html', mensaje=mensaje)
