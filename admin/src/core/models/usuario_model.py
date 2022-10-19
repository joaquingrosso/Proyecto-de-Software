from datetime import datetime
from src.core.database import db
from src.core.models.rol_model import Rol
from werkzeug.security import generate_password_hash , check_password_hash
from src.core.models.rol_model import Rol


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
    password = db.Column(db.String(500))    
    email = db.Column(db.String(50))
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    activo = db.Column(db.Integer) #0 moroso (no) - 1 activo (si)
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
    roles = db.relationship('Rol', secondary=roles, backref=db.backref(
        'usuarios_con_el_rol', lazy=False), lazy='dynamic')
    
    def __init__(
            self, email, username, password, first_name, last_name
    ):
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.activo = 1
        rol = Rol.get_rol_Socio()
        print(rol.nombre)
        self.roles.extend([rol])

    def __repr__(self):
        return "<user(username='%s',email='%s', first_name='%s', last_name='%s' )>" % (
            self.username,
            self.email,
            self.first_name,
            self.last_name,
        )
        
    def listar_roles(self):
        print("entro")
        for rol in roles:
            aux = rol.getNombre()   
        print("listar roles",aux)
        return aux
    
    
    @classmethod
    def get_user_by_id(self, user_id):
        return Usuario.query.filter(self.id == user_id).first()
    
  
    def verify_password(self, password):
        passwd = self.password
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

    def list_usuarios(page,cant):
        return Usuario.query.filter_by().paginate(page,cant)
    
    
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
        
    @classmethod
    def tiene_rol(self,id,permiso):
        valido = False
        user= Usuario.get_user_by_id(id)
        roles = user.roles.all()
        for rol in roles:
           if Rol.tiene_permiso(rol.nombre,permiso):
               valido = True
               break
        #return bool(user.roles.filter_by(id=id).first().permisos.filter_by(nombre=permiso))
        return valido