from datetime import datetime
from src.core.database import db

class Usuario(db.Model):
    
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    nombre_usaurio = db.Column(db.String(30))    
    email = db.Column(db.String(50))
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    password = db.Column(db.String(20))
    activo = db.Column(db.Integer) #0 moroso (no) - 1 activo (si)
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())

