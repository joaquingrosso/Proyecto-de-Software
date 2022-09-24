from cgitb import handler
from logging import handlers

from flask import Flask
from flask import render_template

from src.web.helpers import handlers
from src.web.config import config
from src.core import database

# def create_app(static_folder="static"):
def create_app(env="development", static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)

    app.config.from_object(config[env])

    database.init_app(app)

    @app.get("/")
    def home():
        #return "hola mundo"
        return render_template("home.html")   

    app.register_error_handler(404, handlers.not_found_error)
    # app.register_error_handler(500, handlers.internal_server_error)

    @app.cli.command(name="resetdb")
    def resetdb():
        database.reset_db()
        
    return app