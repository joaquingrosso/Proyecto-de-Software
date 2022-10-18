from flask import redirect, render_template, request, url_for, session, flash
from src.core.models.usuario_model import Usuario
from werkzeug.security import check_password_hash


def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session["username"] = username
        session["password"] = password
        #usuario = Usuario.get_by_username_and_pass(request.form['username'], request.form['password'])
        user = Usuario.query.filter_by(username=username).first()
        session["id"]= user.id
        pass1 = user.password
        if user == None:
            flash("el nombre de usuario o contraseña es incorrecto")
        print(user)
        if user:
            if check_password_hash(pass1, password):
                return render_template('inicio_privada.html')
            elif user.password != password:
                flash("el nombre de usuario o contraseña es incorrecto")
            else:
                flash("el nombre de usuario o contraseña es incorrecto")
    return render_template("auth/login.html")               


def logout():
    session.pop("username", None)
    return redirect(url_for("home"))

