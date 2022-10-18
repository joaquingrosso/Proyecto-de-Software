from src.core import models


def run():
       
    #creacion registro configuracion
    config = models.crear_configuracion(
        id = "1",
        cant = "3",
        estado_pagos = "1",  
        info_contacto ="unContacto..", 
        texto_encabezado = "unTexto..",    
        valor_cuota = "unValor..",    
        recargo_cuota = "unRecargo..",
    
        )
    
