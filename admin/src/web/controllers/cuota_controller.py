from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota
from src.core.models.asociado_model import Asociado
from src.core.models.pago_model import Pago
from flask import render_template ,request, redirect, url_for ,flash, make_response, Response
from src.web.controllers import login_required
import pdfkit
import base64



@login_required
def realizar_pago(id_a, id_d):
    cuotas = Cuota.get_cuotas_by_disciplina_asociado(id_d, id_a)
    return render_template("pago_de_una_couta/realizar_pago.html", cuotas = cuotas) 

@login_required
def pagar_cuota(id_c, monto, id_d, id_a):
    cuo = Cuota.get_cuota_by_id(id_c)
    cuo.estado = Cuota.get_estado_paga()
    cuo.register_cuota_database()

    register_pago_database(id_c, monto, cuo.periodo)

    cuotas = Cuota.get_cuotas_by_disciplina_asociado(id_d, id_a)
    return render_template("pago_de_una_couta/realizar_pago.html", cuotas = cuotas) 


def register_pago_database(id_c, monto, periodo):
    pago = Pago(id_c, monto, periodo)
    pago.register_pago_database()       
    return redirect(url_for("gestion_asociados"))  



def ver_recibo_cuota(cuota_id):
    cuota = Cuota.get_cuota_by_id(cuota_id)
    
    # with open("logo.jpg", "rb") as img_file:
    #     my_string = base64.b64encode(img_file.read())
     


    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    html = render_template('/pdfs/pdf_recibo_cuota.html', cuota=cuota)
    pdf = pdfkit.from_string(html,False,configuration=config)
    resp = make_response(pdf)
    resp.headers["Content-Type"] = "aplication/pdf"
    resp.headers["Content-Disposition"] = "inline;filename=recibo_cuota.pdf"
    return resp
    