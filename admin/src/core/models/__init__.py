from src.core.database import db
from src.core.models.config_model import Config
from src.core.models.permiso_model import Permiso
from src.core.models.rol_model import Rol
from src.core.models.usuario_model import Usuario
from src.core.models.asociado_model import Asociado

def crear_configuracion(**kwargs):
    config = Config(**kwargs)
    db.session.add(config)
    db.session.commit()
    return config

def crear_permisos(**kwargs):
    permiso = Permiso(**kwargs)
    db.session.add(permiso)
    db.session.commit()
    return permiso

def crear_roles(**kwargs):
    rol = Rol(**kwargs)
    db.session.add(rol)
    db.session.commit()
    return rol

def crear_usuario(**kwargs):
    user = Usuario(**kwargs)
    db.session.add(user)
    db.session.commit()
    return user

def crear_asociado(**kwargs):
    asociado = Asociado(**kwargs)
    db.session.add(asociado)
    db.session.commit()
    return asociado

def asignar_permisos(rol,permisos):
    rol.permisos.extend(permisos)
    db.session.add(rol)
    db.session.commit()
    return rol

def asignar_usuario(usuario,rol1):
    usuario.roles.extend(rol1)
    db.session.add(usuario)
    db.session.commit()
    return usuario



def asignar_asociado(asociado,disciplina):
    asociado.disciplinas.extend(disciplina)
    db.session.add(asociado)
    db.session.commit()
    return asociado
