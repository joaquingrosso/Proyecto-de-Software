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
    print("el recargo es:", recargo_cuota)
    dia_actual=int(fecha_hoy.strftime('%d'))
    mes_actual=int(fecha_hoy.strftime('%m'))
    if dic_mes.get(cuo.periodo) <= mes_actual:
        if dia_actual >= 1 and dia_actual <= 10:
            # cuo.register_cuota_database()
            # register_pago_database(id_c, monto, cuo.periodo)
            print("no es")
        else:
            print("es moroso")
    else:
        print("se fue al else")
    cuo.register_cuota_database()
    register_pago_database(id_c, monto, cuo.periodo)
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
    print(encabezado)

    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    html = render_template('/pdfs/pdf_recibo_cuota.html', pago = pago, encabezado = encabezado, asociado=asociado)
    pdf = pdfkit.from_string(html,False,configuration=config)
    resp = make_response(pdf)
    resp.headers["Content-Type"] = "aplication/pdf"
    resp.headers["Content-Disposition"] = "inline;filename=recibo_cuota.pdf"
    return resp
    