from flask import session, abort
from src.web.helpers.auth import authenticated
from src.core.models.usuario_model import Usuario

def validar_permisos(id,permiso):
	return Usuario.tiene_rol(id, permiso)


########   Funciones auxiliares   ########
def es_admin(id):
	valido = False
	user = Usuario.get_user_by_id(id)
	roles = user.roles
	for r in roles:
		if r.nombre != "Administrador":
			valido = True
		break
	return valido

def no_es_admin():
	return not (authenticated(session) and Usuario.tiene_rol(session["usuario"], 'admin'))


def no_tiene_el_permiso_solicitado(un_permiso):
	return not session["usuario"].tiene_permiso(un_permiso)

def usuario_activo(session):
	return session["usuario"].activo