from datetime import datetime
from src.core.database import db

cuotas_asociados = db.Table('usuario_tiene_cuota',
                 db.Column('asociado_id', db.Integer, db.ForeignKey(
                     'asociado.id')),
                 db.Column('cuota_id', db.Integer, db.ForeignKey(
                     'cuota.id'))
                 )

class Cuota(db.Model):
    __tablename__ = 'cuota'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    #asociado_id = db.Column(db.Integer, db.ForeignKey('asociado.id'),nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'),nullable=False)    
    monto = db.Column(db.Integer)
    periodo = db.Column(db.String, unique=False, nullable=False)
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
    asociados_cuotas = db.relationship('Asociado', secondary=cuotas_asociados, backref=db.backref('usuario_tiene_cuota', lazy = False), lazy='dynamic')

    def __init__(
        self, asociado_id, disciplina_id, monto, periodo):

        self.asociado_id = asociado_id,
        self.disciplina_id = disciplina_id,
        self.monto = monto,
        self.periodo = periodo
    
    # def __repr__(self):
    #     return "<cuota(first_name='%s', last_name='%s', member_number='%s' )>" % (
    #         self.first_name,
    #         self.last_name,
    #         self.member_number,
    #     )

    @classmethod
    def get_cuota_by_id(self, cuota_id):
        return Cuota.query.filter(self.id == cuota_id).first()
    

    def list_cuota():
        return Cuota.query.all()