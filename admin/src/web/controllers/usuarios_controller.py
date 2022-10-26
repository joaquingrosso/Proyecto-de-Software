from src.core.models.usuario_model import Usuario
from flask import render_template ,request, redirect, url_for ,flash 
from werkzeug.security import generate_password_hash , check_password_hash
from src.web.controllers import login_required
from src.core.models.rol_model import Rol
from src.core.models.config_model import Config

@login_required
def crear_usuario():

    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        if not verify_user(username, email) and verify_lenghts(username, password, email, first_name , last_name): #se chequea que el usuario no exista y y el tamaño de los campos
            register_database(email, username, password, first_name, last_name)
            return redirect(url_for("gestion_usuarios"))  
    return render_template('user/crear_usuario.html')

@login_required    
def eliminar_usuario(id):
    usu = Usuario.get_user_by_id(id)
    usu.delete()
    return redirect(url_for("gestion_usuarios"))

@login_required
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
        if valido:
            if usu.username != username:
                if verify_username(username):
                    valido = False

            if usu.email != email:
                if verify_email(email):
                    valido = False
            if verify_lenghts(username, None, email, first_name , last_name):
                usu.update_user_database(first_name,last_name,email,username)
                return redirect(url_for("gestion_usuarios"))  
    # return render_template('/user/modificar_usuario.html', usu=usu) 
        return redirect(url_for("gestion_usuarios"))    
    return redirect(url_for("gestion_usuarios"))  

@login_required
def activar_desactivar(id):
    user = Usuario.get_user_by_id(id)
    if user.activo == Usuario.get_estado_activo():
        user.activo = Usuario.get_estado_no_activo()
    else:
        user.activo = Usuario.get_estado_activo()
    user.register_user_database()
    return redirect(url_for("gestion_usuarios"))

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
        #se chequea que el usuario no exista y que no tenca campos vacios
        
        if not verify_user(username, email) and verify_lenghts(username, password, email, first_name , last_name) and valido: 
            register_database(email, username, password, first_name, last_name,)
            return redirect(url_for("login"))
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

def verify_lenghts(username, password, email, first_name, last_name):
    #username
    if len(username) == 0:
        flash("Nombre de usuario vacio, complete el campo")
        return False
    else:
        if len(username) > 30:
            flash("Nombre de usuario muy largo")
            return False
        elif len(username) < 5:
            flash("Nombre de usuario muy corto")
            return False   
    #password
    if password == 0:
        if len(password) > 20:
            flash("Contraseña muy larga")
            return False
        elif len(password) < 6:
            flash("Contraseña muy corta")
            return False       
    #email
    if len(email) == 0:
        flash("Email de usuario vacio, complete el campo")
        return False
    else:
        if len(email) > 50:
            flash("Email muy largo")
            return False
        elif len(email) < 15:
            flash("Email muy corto")
            return False   
    #nombre
    if len(first_name) == 0:
        flash("Nombre vacio, complete el campo")
        return False
    else:
        if len(first_name) > 10:
            flash("Nombre muy largo")
            return False
        elif len(first_name) < 5:
            flash("Nombre muy corto")
            return False 
    #apellido
    if len(last_name) == 0:
        flash("Apellido vacio, complete el campo")
        return False
    else:
        if len(last_name) > 30:
            flash("Apellido muy largo")
            return False
        elif len(last_name) < 5:
            flash("Apellido muy corto")
            return False 

    return True

def register_database(email,username,password, first_name,last_name):
    passwd_hash = generate_password_hash(password)
    user= Usuario(email,username,passwd_hash, first_name, last_name)
    user.register_user_database()
    return render_template('user/register_user.html')

@login_required
def agregar_rol(id):
    user = Usuario.get_user_by_id(id)
    roles_usuario = list(user.roles)
    cantidad_roles =len(roles_usuario)
    if request.method == "POST":
        valor_select = request.form.get('roles')
        if cantidad_roles != 3 and validar_rol(roles_usuario,valor_select):
            rol = Rol.obtener_rol(valor_select)
            user.roles.extend([rol])
            user.register_user_database()
        else:
            if cantidad_roles == 3:
                flash("Ya tiene todos los roles disponibles y no se pueden agregar mas")
    return redirect(url_for("gestion_usuarios"))

def validar_rol (roles_user,valor):
    for rol in roles_user:
        if rol.nombre == valor:
            flash("El usuario ya posee el rol")
            return False
    return True


def buscar_usuario():
    page = request.args.get('page', 1, type=int)
    config = Config.get_self(Config, 1)

    lista_usuario = Usuario.search_by_status(request.args['estado'],page,config.cant)
    results = Usuario.get_paginated(Usuario, lista_usuario, page, config.cant)

    return render_template("gestion_usuarios.html", user=results)

def validar_rol_eliminar (roles_user,valor):
    encontre = True
    for rol in roles_user:
        if rol.nombre == valor:
            encontre = False
            return False
    if encontre:
        flash("El rol seleccionado no lo tiene asignado el usuario")
    else:
        flash("Se elimino el rol satisfactoriamente")
    return True

def eliminar_rol(id):
    user = Usuario.get_user_by_id(id)
    roles_usuario = list(user.roles)
    cantidad_roles =len(roles_usuario)
    if request.method == "POST":
        valor_select = request.form.get('roles')
        print(Rol.obtener_rol(valor_select))
        if not validar_rol_eliminar(roles_usuario,valor_select):
            if cantidad_roles > 1 and cantidad_roles <= 3:
                rol = Rol.obtener_rol(valor_select)
                user.roles.remove(rol)
                user.register_user_database()
            else:
                flash("No se puede eliminar el rol ya que elimino la cantidad de roles maxima")
    return redirect(url_for("gestion_usuarios"))
