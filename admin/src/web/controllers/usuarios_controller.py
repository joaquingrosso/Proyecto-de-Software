from src.core.models.usuario_model import Usuario
from flask import render_template ,request, redirect, url_for ,flash 
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

def verify_username(username):    
    usuario = Usuario.query.filter_by(username=username).first()
    print(usuario)
    if usuario is not None:
        flash("El usuario ingresado ya existe")
        return True
    return False

def verify_email(email):
    email = Usuario.query.filter_by(email = email).first()
    if email is not None:
        flash("El email ingresado ya existe")
        return True
    return False

def register_database(email,username,password, first_name,last_name):
    passwd_hash = generate_password_hash(password)
    passwd1= passwd_hash[:len(passwd_hash)//2]
    passwd2= passwd_hash[len(passwd_hash)//2:]
    user= Usuario(email,username, passwd1,passwd2, first_name, last_name)
    user.register_user_database()
        
    return render_template('user/register_user.html')


def crear_usuario():
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
            return redirect(url_for("gestion_usuarios"))  
    return render_template('user/crear_usuario.html')


    
def eliminar_usuario(id):
    usu = Usuario.get_user_by_id(id)
    usu.delete()
    return redirect(url_for("gestion_usuarios"))

def modificar_usuario(id):
    usu = Usuario.get_user_by_id(id)
    if request.method == "POST":
        valido = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                valido = False
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        username = request.form['username']
<<<<<<< HEAD
        # if usu.username != request.form['username']:
        #     print("paso el primer if username")
        #     if not verify_username(username):
        #         print("paso el segundo if verify_user")
        usu.update_user_database(first_name,last_name,email,username)
        #     return redirect(url_for("gestion_usuarios"))
        if valido:
          usu.update_user_database(first_name,last_name,email,username)
          return redirect(url_for("gestion_usuarios"))  
    # return render_template('/user/modificar_usuario.html', usu=usu) 
        return redirect(url_for("gestion_usuarios")) 
=======
            
        if usu.username != username:
            if verify_username(username):
                valido = False

        if usu.email != email:
            if verify_email(email):
                valido = False
       
        if valido:
          usu.update_user_database(first_name,last_name,email,username)
          return redirect(url_for("gestion_usuarios"))      
    return render_template('/user/modificar_usuario.html', usu=usu)    
    
>>>>>>> be68c228a476287dbff4a4c895117e6cae6ee877
