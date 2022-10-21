from datetime import datetime
from src.core.database import db


class Pago(db.Model):
    __tablename__ = 'pago'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    cuota_id = db.Column(db.Integer, db.ForeignKey('cuota.id'),nullable=False)
    monto = db.Column(db.Integer)
    periodo = db.Column(db.String, unique=False, nullable=False)
    

    def __init__(self, cuota_id, monto, periodo):
        self.cuota_id = cuota_id,
        self.monto = monto,
        self.periodo = periodo
    
    @classmethod
    def pago_asociado(self, id):
        return Pago.query.filter(self.cuota_id == id).first()

    def register_pago_database(self):
            db.session.add(self)
            db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit() 
    @classmethod        
    def eliminar_pagos(self, cuota_id):
        pagos = Pago.pago_asociado(cuota_id)
        if pagos != None:
            self.delete(pagos)