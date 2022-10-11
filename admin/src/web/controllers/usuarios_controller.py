from src.core.models.usuario_model import Usuario
from flask import render_template ,request, redirect, url_for   

def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        user= Usuario(email,username, password, first_name, last_name)
        user.register_user_database()
        
    return render_template('user/register_user.html')


def crear_usuario():
    mensaje = ''
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        if Usuario.existe_usuario(request.form['username']):
            mensaje="El nombre de usuario ya existe"
        else:
            res= user= Usuario(email,username, password, first_name, last_name)
            if res:
                mensaje = "Usuario creado exitosamente"
                user.register_user_database()
            else:
                mensaje = "Hubo algun problema"
            return render_template('/gestion_usuarios.html', mensaje= mensaje)
        return render_template('user/crear_usuario.html', mensaje= mensaje)
    else:
        return render_template('user/crear_usuario.html', mensaje=mensaje)

    
def eliminar_usuario(id):
    print("entro! eliminar controller")
    usu = Usuario.get_user_by_id(id)
    usu.delete()
    return redirect(url_for("gestion_usuarios"))
