from datetime import datetime
from src.core.database import db

class Cuota(db.Model):
    
    __tablename__ = 'cuota'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    asociado_id = db.Column(db.Integer, db.ForeignKey('asociado.id'),nullable=False)
    disciplina_id = db.Column(db.Integer, db.ForeignKey('disciplina.id'),nullable=False)    
    monto = db.Column(db.Integer)
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())

    # agregar un campo peiodo
    # falta una tabla pagos , que este asociado a una couta


    def __init__(
            self, asociado_id=None, disciplina_id=None, monto=None
    ):
        self.first_name = asociado_id
        self.disciplina_id = disciplina_id
        self.monto = monto
    
    # def __repr__(self):
    #     return "<cuota(first_name='%s', last_name='%s', member_number='%s' )>" % (
    #         self.first_name,
    #         self.last_name,
    #         self.member_number,
    #     )


    def list_cuota():
        return Cuota.query.all()