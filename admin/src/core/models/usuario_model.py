from datetime import datetime
from src.core.database import db
from src.core.models.rol_model import Rol
from werkzeug.security import generate_password_hash , check_password_hash
from src.core.models.rol_model import Rol
from sqlalchemy import Column, Boolean


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
    activo = db.Column(db.String(10)) #activo no-activo
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())
    roles = db.relationship('Rol', secondary=roles, backref=db.backref(
        'usuarios_con_el_rol', lazy=False), lazy='dynamic')
    asociado_id = db.Column(db.Integer, db.ForeignKey('asociado.id'),nullable=True)
    
    def __init__(
            self, email, username, password, first_name, last_name , asociado_id = None, 
    ):
        self.email = email
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.activo = "Activo"
        rol = Rol.get_rol_Socio()
        self.roles.extend([rol])
        self.asociado_id= asociado_id

    def __repr__(self):
        return "<user(username='%s',email='%s', first_name='%s', last_name='%s',asociado_id='%s' )>" % (
            self.username,
            self.email,
            self.first_name,
            self.last_name,
            self.asociado_id
        )
        
    def listar_roles(self):
        for rol in roles:
            aux = rol.getNombre()   
        return aux
    
    @classmethod
    def set_asociado_id(self,id):
        self.asociado_id = id
    
    @classmethod
    def get_estado_activo(self):
        return "Activo"

    @classmethod
    def get_estado_no_activo(self):
        return "Desactivo"
    
    @classmethod
    def get_user_by_id(self, user_id):
        return Usuario.query.filter(self.id == user_id).first()            
        
    @classmethod
    def get_user_by_username_and_password(self, username, password):
        return Usuario.query.filter(self.username == username, self.password == password).first()

    @classmethod
    def get_user_by_username(self, username):
        return Usuario.query.filter(self.username == username).first()
    
    @classmethod
    def get_socios_activos(self):
        usuarios_activos = Usuario.query.filter(self.activo == "Activo")
        usuarios = []
        for u in usuarios_activos:
            for r in u.roles:
                if r.nombre == "Socio":
                    usuarios.append(u)
            
        return usuarios
    def verify_password(self, password):
        passwd = self.password
        return check_password_hash(passwd, password)

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


    def search_by_status(estado,page,cant):
        if estado == 'all':
            return Usuario.query.filter_by()
        return Usuario.query.filter_by(activo=estado) 

    def get_paginated(self, query, page, cant):
        return query.filter_by().paginate(page=page, per_page=cant)

    def vincular_usuario_socio(self,asociado_id):
        self.asociado_id = asociado_id
        db.session.commit()
        
    def get_id_asociado():
        return self.asociado_id