from datetime import datetime
from src.core.database import db

pago_cuotas = db.Table('cuota_tiene_pago',
                 db.Column('asociado_id', db.Integer, db.ForeignKey(
                     'asociado.id')),
                 db.Column('pago_id', db.Integer, db.ForeignKey(
                     'pago.id')),
                 db.Column('cuota_id', db.Integer, db.ForeignKey(
                     'cuota.id'))
                 )

class Pago(db.Model):
    __tablename__ = 'pago'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    asociado_id = db.Column(db.Integer, db.ForeignKey('asociado.id'),nullable=False)
    cuota_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'),nullable=False)    
    pago_cuotas = db.relationship('Cuota', secondary=pago_cuotas, backref=db.backref('cuota_tiene_pago', lazy = False), lazy='dynamic')




def register_pago_database(self):
        db.session.add(self)
        db.session.commit()