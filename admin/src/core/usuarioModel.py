from datetime import datetime
from src.core.database import db

class Usuario(db.Model):
    
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(50))   
    email = db.Column(db.String(50))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    activo = db.Column(db.Integer) #0 moroso (no) - 1 activo (si)
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(
            self, email=None, username=None, password=None, first_name=None, last_name=None
    ):
        self.email = ((email),)
        self.username = ((username),)
        self.password = ((password),)
        self.first_name = ((first_name),)
        self.last_name = ((last_name),)
        self.activo = 1

    def __repr__(self):
        return "<user(username='%s', first_name='%s', last_name='%s' )>" % (
            self.username,
            self.first_name,
            self.last_name,
        )

    def esta_activo(self):
        return self.activo