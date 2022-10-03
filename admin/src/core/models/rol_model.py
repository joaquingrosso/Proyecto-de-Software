from src.core.database import db

class Rol(db.Model):
    
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40))
    
    def __init__(self , nombre = None):
        self.nombre = nombre