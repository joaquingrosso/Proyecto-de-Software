from flask import session, abort
from src.web.helpers.auth import authenticated
from src.core.models.usuario_model import Usuario

def validar_permisos(id,permiso):
	# if no_es_admin():
	# 	print("Salio xq no esta logueado como admin")
	# 	abort(503)

	# # Si el usuario no tiene una cookie de sesion válida muestro un mensaje de error
	# if not authenticated(session):
	# 	print("Salio xq no estaba autenticado")
	# 	abort(401)
	# if not usuario_activo(session):
	# 	print("Salio xq no estaba activo")
	# 	abort(403)
	# if un_permiso != '' and no_tiene_el_permiso_solicitado(un_permiso):
	# 	print("Se solicito permiso para "+un_permiso)
	# 	print("Salio xq no tenia el permiso")
	# 	abort(403)
	return Usuario.tiene_rol(id, permiso)


########   Funciones auxiliares   ########

def no_es_admin():
	return not (authenticated(session) and Usuario.tiene_rol(session["usuario"], 'admin'))


def no_tiene_el_permiso_solicitado(un_permiso):
	return not session["usuario"].tiene_permiso(un_permiso)

def usuario_activo(session):
	return session["usuario"].activo