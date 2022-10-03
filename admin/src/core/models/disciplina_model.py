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
        self.name = ((name),)
        self.category = ((category),)
        self.instructors = ((instructors),)
        self.date_time = ((date_time),)
        self.monthly_cost = ((monthly_cost),)
        self.enabled = ((enabled),)

    def __repr__(self):
        return "<disciplina(name='%s', date_time='%s', monthly_cost='%s' )>" % (
            self.name,
            self.date_time,
            self.monthly_cost,
        )


    def list_disciplina():
        return Disciplina.query.all()