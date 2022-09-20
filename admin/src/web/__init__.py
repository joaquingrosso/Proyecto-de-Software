from flask import Flask
from flask import render_template

def create_app(static_folder="static"):
    app = Flask(__name__, static_folder=static_folder)

    @app.get("/")
    def home():
        #return "hola mundo"
        return render_template("home.html")

    return app