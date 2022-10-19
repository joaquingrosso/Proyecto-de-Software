from datetime import datetime
from enum import unique
from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota
from src.core.database import db
from src.core import models

asociado_disciplina = db.Table ("asociado_disciplina",
    db.Column ("asociado_id",db.Integer,db.ForeignKey ("asociado.id"), primary_key=True),
    db.Column ("disciplina_id",db.Integer,db.ForeignKey ("disciplina.id"), primary_key=True)
)

# asociado_cuota = db.Table( "asociado_cuota",
                          
#     db.Column ("asociado_id",db.Integer,db.ForeignKey ("asociado.id"), primary_key=True),
#     db.Column ("disciplina_id",db.Integer,db.ForeignKey ("disciplina.id"), primary_key=True) 
    
# )

class Asociado(db.Model):
    
    __tablename__ = 'asociado'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    document_type = db.Column(db.String(5))
    document = db.Column(db.String(15))
    gender = db.Column(db.String(15))
    #member_number = db.Column(db.Integer, unique=True) representado con el id
    adress = db.Column(db.String(50))
    state = db.Column(db.String(10))
    phone_number = db.Column(db.Integer)
    email = db.Column(db.String(50))
    disciplinas = db.relationship('Disciplina', secondary=asociado_disciplina, backref=db.backref('asociado_realiza_disciplina', lazy = False), lazy='dynamic')
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
    #cuota = db.relationship('cuota', secondary=asociado_cuota, backref=db.backref('asociado_realiza_una_cuota', lazy = True), lazy='subquery')

    def __init__(
            self, first_name=None, last_name=None, document_type=None, document=None, gender=None, adress=None, state=None ,phone_number=None , email=None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.document_type = document_type
        self.document = document
        self.gender = gender
        #self.member_number = member_number
        self.adress = adress
        self.state = state
        self.phone_number = phone_number
        self.email = email

    def __repr__(self):
        return "<asociado(first_name='%s', last_name='%s')>" % (
            self.first_name,
            self.last_name,
    
        )

    @classmethod
    def get_asociado_by_id(self, asoc_id):
        return Asociado.query.filter(self.id == asoc_id).first()

    @classmethod
    def get_asociado_by_document(self, doc, doc_type):
        return Asociado.query.filter(self.document == doc, self.document_type == doc_type).first()

    @classmethod
    def tiene_disciplina(self, id, id_disc):
        asociado = Asociado.get_asociado_by_id(id)
        disciplinas = asociado.disciplinas
        if list(disciplinas) == []:
            return False
        else:
            return bool(disciplinas.filter_by(id = id_disc).first())
   
    @classmethod
    def inscribir_disciplina(self,asociado, disciplina):
        models.asignar_asociado(asociado, [disciplina])

    def update_asociado_database(self, first_name, last_name, document_type, document, gender, adress, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.document_type = document_type
        self.document = document
        self.gender = gender
        self.adress = adress
        #self.state = state
        self.phone_number = phone_number
        self.email = email
        db.session.commit()

    def register_asociado_database(self):
        db.session.add(self)
        db.session.commit()

    def list_asociados(page,cant):
        return Asociado.query.filter_by().paginate(page,cant)

    def delete(self):
        db.session.delete(self)
        db.session.commit()