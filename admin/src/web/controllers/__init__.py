from flask import Flask
from flask import render_template, request, redirect , url_for, flash, session
from functools import wraps

def login_required(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if 'logged_in' in session:
                return f(*args, **kwargs)
            else:
                flash('Es necesario iniciar sesion para acceder a la aplicacion')
                return redirect(url_for('login'))
        return wrap