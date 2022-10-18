from src.core.database import db

class Permiso(db.Model):
    __tablename__= 'permiso'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(40))
    
    def __init__(self, nombre):
        self.nombre = nombre
        
    
    def register_database(self):
        db.session.add(self)
        db.session.commit()