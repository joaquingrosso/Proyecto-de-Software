from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota
from src.core.models.asociado_model import Asociado
from src.core.models.pago_model import Pago
from flask import render_template ,request, redirect, url_for ,flash, make_response, Response
from src.web.controllers import login_required
import pdfkit
import base64
from datetime import datetime 
from src.core.models.config_model import Config
from flask import current_app as app

@login_required
def realizar_pago(id_a, id_d):
    cuotas = Cuota.get_cuotas_by_disciplina_asociado(id_d, id_a)
    return render_template("pago_de_una_couta/realizar_pago.html", cuotas = cuotas) 

@login_required
def pagar_cuota(id_c, monto, id_d, id_a):
    dic_mes={ "Enero":1, "Febrero":2, "Marzo":3, "Abril":4, "Mayo":5, "Junio":6,
             "Julio":7, "Agosto":8, "Septembre":9, "Octubre":10, "Noviembre":11, "Diciembre":12}
    cuo = Cuota.get_cuota_by_id(id_c)
    cuo.estado = Cuota.get_estado_paga()
    fecha_hoy = datetime.now()
    recargo_cuota = Config.get_valor_porcentaje()
    dia_actual=int(fecha_hoy.strftime('%d'))
    mes_actual=int(fecha_hoy.strftime('%m'))
    if dia_actual >= 1 and dia_actual <= 10:
        cuo.register_cuota_database()
        register_pago_database(id_c, monto, cuo.periodo)
        flash("Se realizo el pago correctamente")
    else:
        recargo = (cuo.monto * recargo_cuota)/100
        monto_recargo = cuo.monto + recargo
        msg= f"Al realizar el pago con vencimiento aplicandose el %{recargo_cuota} de interes quedando su valor en: {monto_recargo}"
        flash(msg)
        cuo.monto = monto_recargo
        cuo.register_cuota_database()
        register_pago_database(id_c, monto_recargo, cuo.periodo)
    cuotas = Cuota.get_cuotas_by_disciplina_asociado(id_d, id_a)
    return render_template("pago_de_una_couta/realizar_pago.html", cuotas = cuotas) 


def register_pago_database(id_c, monto, periodo):
    pago = Pago(id_c, monto, periodo)
    pago.register_pago_database()       
    return redirect(url_for("gestion_asociados"))  



def ver_recibo_cuota(cuota_id):
    # with open("logo.jpg", "rb") as img_file:
    #     my_string = base64.b64encode(img_file.read())
    
    #id de pago - fecha de pago - encabezado config - importe y periodo pago
    pago = Pago.pago_de_una_cuota(cuota_id)
    encabezado = Config.get_self(Config, 1).texto_encabezado
    cuota = Cuota.get_cuota_by_id(cuota_id)
    asociado = cuota.get_nombre_asociado()
    fecha_hoy = datetime.now()
    dia = fecha_hoy.strftime('%d')
    mes = fecha_hoy.strftime('%m')
    año = fecha_hoy.strftime('%Y')
    fecha = dia +"/" + mes + "/" + año
    if app.config.get("USE_WKHTML_CUSTOM_PATH") == True:
        path_wkhtmltopdf = app.config.get("WKHTML_CUSTOM_PATH")
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)    
        html = render_template('/pdfs/pdf_recibo_cuota.html', pago = pago, encabezado = encabezado, asociado=asociado, fecha=fecha)
        pdf = pdfkit.from_string(html,False,configuration=config)
        
    else:
        html = render_template('/pdfs/pdf_recibo_cuota.html', pago = pago, encabezado = encabezado, asociado=asociado, fecha=fecha)
        pdf =pdfkit.from_string(html,False)
    resp = make_response(pdf)
    resp.headers["Content-Type"] = "aplication/pdf"
    resp.headers["Content-Disposition"] = "inline;filename=recibo_cuota.pdf"
    return resp
    
# @classmethod
# def estado_asociado(self, asociadoid):
#     pago= False
#     cuotas_asociado = Cuota.get_cuota_by_id_asociado(asociadoid)
#     dic_mes={ "Enero":1, "Febrero":2, "Marzo":3, "Abril":4, "Mayo":5, "Junio":6,
#              "Julio":7, "Agosto":8, "Septembre":9, "Octubre":10, "Noviembre":11, "Diciembre":12}
#     fecha_hoy = datetime.now()
#     dia_actual=int(fecha_hoy.strftime('%d'))
#     mes_actual=int(fecha_hoy.strftime('%m'))
#     for cuota in cuotas_asociado:
#         mes = cuota.periodo.split(" ")
#         if dic_mes[mes[0]] <= mes_actual and cuota.estado == "Paga":
#     return False