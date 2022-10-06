from datetime import datetime
from src.core.database import db

roles = db.Table('usuario_tiene_rol',
                 db.Column('usuario_id', db.Integer, db.ForeignKey(
                     'usuario.id')),
                 db.Column('rol_id', db.Integer, db.ForeignKey(
                     'rol.id'))
                 )

class Usuario(db.Model):
    
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(50))   
    email = db.Column(db.String(50))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    activo = db.Column(db.Integer) #0 moroso (no) - 1 activo (si)
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
    roles = db.relationship('Rol', secondary=roles, backref=db.backref(
        'usuarios_con_el_rol', lazy=True), lazy='subquery')
    
    def __init__(
            self, email=None, username=None, password=None, first_name=None, last_name=None
    ):
        self.email = ((email),)
        self.username = ((username),)
        self.password = ((password),)
        self.first_name = ((first_name),)
        self.last_name = ((last_name),)
        self.activo = 1

    def __repr__(self):
        return "<user(username='%s', first_name='%s', last_name='%s' )>" % (
            self.username,
            self.first_name,
            self.last_name,
        )

    @classmethod
    def get_user_by_username_and_password(self, username, password):
        return Usuario.query.filter(self.username == username, self.password == password).first()

    @classmethod
    def get_user_by_username(self, username):
        return Usuario.query.filter(self.username == username).first()

    def register_user_database(self):
        db.session.add(self)
        db.session.commit()
        
    def is_valid(self):
        return self.activo and not self.baja

    def list_usuarios():
        return Usuario.query.all()