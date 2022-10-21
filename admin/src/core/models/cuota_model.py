
from datetime import datetime
from src.core.database import db

from src.core.models.asociado_model import Asociado
from src.core.models.disciplina_model import Disciplina
from src.core.models.pago_model import Pago

cuotas_asociados = db.Table('usuario_tiene_cuota',
                 db.Column('asociado_id', db.Integer, db.ForeignKey(
                     'asociado.id')),
                 db.Column('cuota_id', db.Integer, db.ForeignKey(
                     'cuota.id'))
                 )

class Cuota(db.Model):
    __tablename__ = 'cuota'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    asociado_id = db.Column(db.Integer, db.ForeignKey('asociado.id'),nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'),nullable=False)    
    monto = db.Column(db.Integer)
    periodo = db.Column(db.String, unique=False, nullable=False)
    estado = db.Column(db.String(10)) #Paga No-Paga
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
    #asociados_cuotas = db.relationship('Asociado', secondary=cuotas_asociados, backref=db.backref('usuario_tiene_cuota', lazy = False), lazy='dynamic')

    def __init__(self, asociado_id, disciplina_id, monto, periodo):
        self.asociado_id = asociado_id,
        self.disciplina_id = disciplina_id,
        self.monto = monto,
        self.periodo = periodo,
        self.estado = "No-Paga"
    
    # def __repr__(self):
    #     return "<cuota(first_name='%s', last_name='%s', member_number='%s' )>" % (
    #         self.first_name,
    #         self.last_name,
    #         self.member_number,
    #     )

    @classmethod
    def get_cuota_by_id(self, cuota_id):
        return Cuota.query.filter(self.id == cuota_id).first()
    
    @classmethod
    def get_cuotas_by_disciplina_asociado(self, disciplina_id, asociado_id):
        return Cuota.query.filter(self.disciplina_id == disciplina_id, self.asociado_id == asociado_id).order_by(self.id)

    @classmethod
    def get_estado_paga(self):
        return "Paga"

    @classmethod
    def get_estado_no_paga(self):
        return "No-Paga"

    @classmethod
    def cuota_asociado(self, id):
        return Cuota.query.filter(self.asociado_id == id).all()

    @classmethod
    def eliminar_cuotas_asociado(self,id):
        cuotas = Cuota.cuota_asociado(id)
        if cuotas != None :     
            for c in cuotas:
                Pago.eliminar_pagos(c.id)
                c.delete()
    
    @classmethod
    def cuota_disciplina(self, id):
        return Cuota.query.filter(self.disciplina_id == id).all() 
            
    @classmethod
    def eliminar_disciplinas_cuota_asociado(self,id):
        disciplina = Cuota.cuota_disciplina(id)
        if disciplina != None :     
            for d in disciplina:
                Pago.eliminar_pagos(d.id)
                d.delete()
        
    def get_nombre_asociado(self):
        return Asociado.get_nombre_by_id(self.asociado_id)
    
    def get_nombre_disciplina(self):
        return Disciplina.get_nombre_by_id(self.disciplina_id)

    def register_cuota_database(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_cuota(self,cuota):
        cuota.delete()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def list_cuota():
        return Cuota.query.all()
    
   
        