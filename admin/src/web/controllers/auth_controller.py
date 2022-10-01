from flask import redirect, render_template, request, url_for, session, flash
from src.core.models.usuario_model import Usuario

def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session["username"] = username
        session["password"] = password
        #usuario = Usuario.get_by_username_and_pass(request.form['username'], request.form['password'])
        user = Usuario.query.filter_by(username=username).first()
        if user == None:
            flash("el nombre de usuario o contraseña es incorrecto")
        print(user)
        if user:
            if user.password == password:
                return render_template("index.html")  
            elif user.password != password:
                flash("el nombre de usuario o contraseña es incorrecto")
            else:
                flash("el nombre de usuario o contraseña es incorrecto")
                return redirect(url_for("auth/login"))
    return render_template("auth/login.html")               


def logout():
    session.pop("username", None)
    return redirect(url_for("home"))
