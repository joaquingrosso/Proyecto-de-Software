from flask import redirect, render_template, request, url_for, session,flash
from src.core.models.config_model import Config
from src.core.models.cuota_model import Cuota



def update():
   config = Config.get_self(Config, 1)

   if request.form['cant']:
      cant = request.form['cant']
   if request.form['estado_pagos']:    
      estado_pagos = request.form['estado_pagos']
   if request.form['info_contacto']:
      info_contacto = request.form['info_contacto']
   if request.form['texto_encabezado']:
      texto_encabezado = request.form['texto_encabezado']
   if request.form['valor_cuota']:    
      valor_cuota = request.form['valor_cuota']
   if request.form['recargo_cuota']:
      recargo_cuota = request.form['recargo_cuota']
   if Config.get_valor_cuota() != valor_cuota:
      Cuota.actualizar_monto_cuotas_impagas(valor_cuota)
      flash("Se actualizo el valor de las cuotas no pagas de todas las disciplinas")
   config.update_config_database(cant,estado_pagos,info_contacto,texto_encabezado,valor_cuota,recargo_cuota)


   return redirect(url_for("configuracion"))
