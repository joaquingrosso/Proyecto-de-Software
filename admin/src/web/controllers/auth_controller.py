from flask import redirect, render_template, request, url_for, session, flash, jsonify
from src.core.models.usuario_model import Usuario
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, set_refresh_cookies
from flask_jwt_extended import unset_jwt_cookies, jwt_required
from flask_jwt_extended import get_jwt_identity

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session["username"] = username
        session["password"] = password
        session['logged_in'] = True
        #usuario = Usuario.get_by_username_and_pass(request.form['username'], request.form['password'])
        user = Usuario.query.filter_by(username=username).first()        
        if user == None or password == None:
            flash("el nombre de usuario o contraseña es incorrecto")     
        if user:
            session["id"] = user.id
            pass1 = user.password
            if check_password_hash(pass1, password) and user.activo != "Desactivo":
                #return render_template('inicio_privada.html', id_usuario = user.id)
                return render_template('inicio_privada.html')
            elif user.activo == "Desactivo":
                flash("El usuario se encuentra Desactivado")
            elif user.password != password:
                flash("el nombre de usuario o contraseña es incorrecto")
           
            else:
                flash("el nombre de usuario o contraseña es incorrecto")

    return render_template("auth/login.html")               


def logout():
    session.clear()
    return redirect(url_for("home"))


# def login_jwt():
#   data = request.get_json()
#   email = data['email']
#   password = data['password']
#   user = Usuario.find_user_by_email_and_pass(email, password)

#   if user:
#     access_token = create_access_token(identity=user.id)
#     response = jsonify()
#     set_access_cookies(response, access_token)
#     return response, 201
#   else:
#     return jsonify(message="Unauthorized"), 401


# @jwt_required( )
# def logout_jwt():
#   response = jsonify()
#   unset_jwt_cookies(response)
#   return response, 200


# @jwt_required( )
# def user_jwt():
#   current_user = get_jwt_identity()
#   user = Usuario.get_user_by_id(current_user)
#   response = jsonify(user)
#   return response, 200