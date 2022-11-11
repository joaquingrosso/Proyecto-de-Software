from src.core import models
from werkzeug.security import generate_password_hash


def run():
    
    #creacion permisos
    permiso1 = models.crear_permisos(nombre="index")
    permiso2 = models.crear_permisos(nombre="new")
    permiso3 = models.crear_permisos(nombre="destroy")
    permiso4 = models.crear_permisos(nombre="update")
    permiso5 = models.crear_permisos(nombre="show")
    permiso6 = models.crear_permisos(nombre="rol")
    permiso7 = models.crear_permisos(nombre="ver_socio")
    permiso8 = models.crear_permisos(nombre="config")
    
    #creacion roles
    rol1 = models.crear_roles(nombre="Administrador")
    rol2 = models.crear_roles(nombre="Operador")
    rol3 = models.crear_roles(nombre="Socio")
    
    #creacion usuario administrador
    admin = models.crear_usuario(
        public_id = "",
        username = "admin",
        password = generate_password_hash("1234"),     
        email = "admin@gmail.com",
        first_name = "admin",
        last_name ="admin" 
        )

    #creacion registro configuracion
    config = models.crear_configuracion(
        cant = 3,
        estado_pagos = 1,  
        info_contacto ="unContacto", 
        texto_encabezado = "unTexto",    
        valor_cuota = 100,    
        recargo_cuota = 50
    
        )
        
    #asignacion usuario al rol
    models.asignar_usuario(admin,[rol1]) #ademas va a tener el rol asociado porque todos los usuarios se crean con ese rol
    
    #asignacion de roles y permisos
    models.asignar_permisos(rol1, [permiso1, permiso2, permiso3, permiso4, permiso5, permiso6 , permiso8])
    models.asignar_permisos(rol2, [permiso1, permiso2, permiso4,permiso5])
    models.asignar_permisos(rol3, [permiso7])