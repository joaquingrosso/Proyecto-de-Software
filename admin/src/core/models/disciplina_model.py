from datetime import datetime
from src.core.database import db

class Disciplina(db.Model):
    
    __tablename__ = 'disciplina'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50)) 
    category = db.Column(db.String(50)) 
    instructors = db.Column(db.String(50)) 
    date_time = db.Column(db.String(50)) 
    monthly_cost = db.Column(db.Float) 
    enabled = db.Column(db.Boolean) 
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
    # cuota = db.relationship('Cuota', backref='disciplina', lazy=True)
    

    def __init__(
            self, name=None, category=None, instructors=None, date_time=None, monthly_cost=None, enabled=None
    ):
        self.name = name
        self.category = category
        self.instructors = instructors
        self.date_time = date_time
        self.monthly_cost = monthly_cost
        self.enabled = enabled

    def __repr__(self):
        return "<disciplina(name='%s', date_time='%s', monthly_cost='%s' )>" % (
            self.name,
            self.date_time,
            self.monthly_cost,
        )

    @classmethod
    def get_disciplina_by_id(self, disip_id):
        return Disciplina.query.filter(self.id == disip_id).first()

    def update_disciplina_database(self, name, category, instructors , date_time, monthly_cost):
        self.name = name
        self.category = category
        self.instructors = instructors
        self.date_time = date_time
        self.monthly_cost = monthly_cost
        db.session.commit()

    def register_disciplina_database(self):
        db.session.add(self)
        db.session.commit()

    def list_disciplina(page,cant):
        return Disciplina.query.filter_by().paginate(page,cant)

    def delete(self):
        db.session.delete(self)
        db.session.commit()