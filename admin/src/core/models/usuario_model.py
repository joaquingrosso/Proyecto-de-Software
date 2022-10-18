from datetime import datetime
from src.core.database import db
from werkzeug.security import generate_password_hash , check_password_hash


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
    pass1 = db.Column(db.String(128))
    pass2 = db.Column(db.String(128))    
    email = db.Column(db.String(50))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    activo = db.Column(db.Integer) #0 moroso (no) - 1 activo (si)
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
    roles = db.relationship('Rol', secondary=roles, backref=db.backref(
        'usuarios_con_el_rol', lazy=True), lazy='subquery')
    
    def __init__(
            self, email, username, pass1,pass2, first_name, last_name
    ):
        self.email = ((email),)
        self.username = ((username),)
        self.pass1 = ((pass1),)
        self.pass2 = ((pass2),)
        self.first_name = ((first_name),)
        self.last_name = ((last_name),)
        self.activo = 1

    def __repr__(self):
        return "<user(username='%s',email='%s', first_name='%s', last_name='%s' )>" % (
            self.username,
            self.email,
            self.first_name,
            self.last_name,
        )
    
    @classmethod
    def get_user_by_id(self, user_id):
        return Usuario.query.filter(self.id == user_id).first()
    
  
    def verify_password(self, password):
        passwd = self.pass1 + self.pass2
        return check_password_hash(passwd, password)
        
    @classmethod
    def get_user_by_username_and_password(self, username, password):
        return Usuario.query.filter(self.username == username, self.password == password).first()

    @classmethod
    def get_user_by_username(self, username):
        return Usuario.query.filter(self.username == username).first()

    def register_user_database(self):
        db.session.add(self)
        db.session.commit()
        
    def update_user_database(self,first_name, last_name, email , username):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        db.session.commit()
        
    def is_valid(self):
        return self.activo and not self.baja

    def list_usuarios():
        return Usuario.query.filter_by().paginate(1,2)
    
    def existe_usuario(username):
        return Usuario.query.filter_by(username=username).first()

    def create(us, cl, no, ap, em):
        today = datetime.now()
        nuevo_usuario = Usuario(username=us, password=cl, first_name=no, last_name=ap, email=em, activo=1, inserted_at=today, created_at=today )
        db.session.add(nuevo_usuario)
        
        return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()