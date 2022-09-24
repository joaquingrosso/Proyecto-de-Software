from cgitb import handler
from logging import handlers
from flask import Flask
from flask import render_template, request, redirect , url_for 
from src.web.helpers import handlers
from src.core.config import config
from src.core import database
from flask_sqlalchemy import sqlalchemy

# def create_app(static_folder="static"):
def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)
    app.config.from_object(config[env])

    # configuracion de la bd
    database.init_app(app)

    # @app.get("/")
    # def home():
    #     return render_template("home.html")
    #ruta al home
    @app.route("/")
    def home():
        return redirect(url_for("login"))
    
    #ruta al login
    @app.route("/login", methods=["GET" , "POST"])
    def login():
        if request.method == "POST":
            print(request.form['username'])
            print(request.form['password'])
            return render_template("auth/login.html")
        else:
            return render_template("auth/login.html")
       


    app.register_error_handler(404, handlers.not_found_error)

    # @app.cli.command(name="resetdb")
    # def resetdb():
    #     database.reset_db()
        
    return app