from src.core.usuarioModel import Usuario


def list_usuarios():
    return Usuario.query.all()