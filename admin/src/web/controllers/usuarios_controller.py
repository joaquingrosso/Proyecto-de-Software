from src.core.models.usuario_model import Usuario
from flask import render_template ,request

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

