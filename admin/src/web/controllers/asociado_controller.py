from unicodedata import category
from src.core.models.asociado_model import Asociado
from flask import render_template, request, redirect , url_for, flash, make_response
from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota
from src.core.models.config_model import Config
import pdfkit

from src.web.controllers import login_required


@login_required
def crear_asociado():
    if request.method == 'POST':
        valido = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                valido = False
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        document_type = request.form.get('document_type')
        document = request.form.get('document')
        gender = request.form.get('gender')
        #member_number = request.form.get('member_number')
        adress = request.form.get('adress')
        state = request.form.get('state')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        
        #se chequea que el usuario no exista y que no tenca campos vacios
        if not verify_asociado(document, document_type)and verify_lenghts(first_name, last_name, document, adress, email) and valido: 
            register_database(first_name, last_name, document_type, document, gender, adress, state, phone_number, email)
            return redirect(url_for("gestion_asociados"))  
    return render_template('asociado/crear_asociado.html')

@login_required
def eliminar_asociado(id):
    eliminar_cuota_asociado(id)
    asoc = Asociado.get_asociado_by_id(id)        
    asoc.delete()
    return redirect(url_for("gestion_asociados"))

@login_required
def modificar_asociado(id):    
    asoc = Asociado.get_asociado_by_id(id)
    if request.method == "POST":
        valido = True
        for clave,valor in request.form.items():
            if valor == '':
                msg_error = f"El campo {clave} esta vacio"
                flash(msg_error)
                valido = False
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        document_type = request.form.get('document_type')   
        document = request.form.get('document')
        gender = request.form.get('gender')
        adress = request.form.get('adress')
        phone_number = request.form.get('phone_number')
        email = request.form.get('email')
        #validaciones de modificar    
        if verify_lenghts(first_name, last_name, document, adress, email) and not verify_asociado_not_actual(id, document, document_type) and valido:
            asoc.update_asociado_database(first_name, last_name, document_type, document, gender, adress, phone_number, email)
            return redirect(url_for("gestion_asociados")) 
        # return render_template('/user/modificar_usuario.html', usu=usu) 
        return redirect(url_for("gestion_asociados"))  

@login_required
def inscribir_asociado_disciplina(id):    
    config = Config.get_self(Config, 1)
    page = request.args.get('page', 1, type=int)
    disciplinasActuales = Disciplina.list_disciplina(page,config.cant)
    return render_template("asociado/inscribir_asociado_disciplina.html", id=id, disciplinas = disciplinasActuales )

@login_required
def habilitar_deshabilitar(id):
    asoc = Asociado.get_asociado_by_id(id)
    if asoc.state == Asociado.get_estado_habilitado():
        asoc.state = Asociado.get_estado_deshabilitado()
    else:
        asoc.state = Asociado.get_estado_habilitado()
    asoc.register_asociado_database()
    return redirect(url_for("gestion_asociados"))

def realizar_inscripcion(id_a, id_d):
    asociado = Asociado.get_asociado_by_id(id_a)
    disciplina = Disciplina.get_disciplina_by_id(id_d)

    if Asociado.tiene_disciplina(id_a, id_d):
        flash("Ya esta inscripto en esta disciplina")
    else:
        Asociado.inscribir_disciplina(asociado, disciplina)
        #generar cuotas
        periodos = [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septembre", "Octubre", "Noviembre", "Diciembre"]
        for i in range(0, 12):
            cuo = Cuota(asociado.id, disciplina.id, disciplina.monthly_cost, periodos[i])
            cuo.register_cuota_database()
    return redirect(url_for("gestion_asociados"))

def verify_asociado(doc, doc_type):
    asoc = Asociado.get_asociado_by_document(doc, doc_type)    
    if asoc is not None:
        flash("Ya existe un asociado con ese documento")
        return True
    return False   

def verify_asociado_not_actual(asoc_id, doc, doc_type):
    asoc = Asociado.get_asociado_by_document(doc, doc_type)    
    if asoc is not None:
        aux = Asociado.get_asociado_by_id(asoc_id)
        if asoc != aux:
            flash("Ya existe un asociado con ese documento")
            return True
    return False   

def verify_lenghts(first_name, last_name, document, adress, email):
    #name
    if len(first_name) > 30:
        flash("Nombre muy largo")
        return False
    elif len(first_name) < 5:
        flash("Nombremuy corto")
        return False   
    #last_name
    if len(last_name) > 30:
        flash("Apellido muy largo")
        return False
    elif len(last_name) < 5:
        flash("Apellido muy corto")
        return False            
    #document
    if len(document) > 15:
        flash("Documento muy largo")
        return False
    elif len(document) < 8:
        flash("Documento muy corto")
        return False 
    #adress
    if len(adress) > 50:
        flash("Direccion muy larga")
        return False
    elif len(adress) < 5:
        flash("Direccion muy corta")
        return False 
    #phone_number
    if len(email) > 50:
        flash("email muy largo")
        return False
    elif len(email) < 15:
        flash("email muy corto")
        return False 
    return True

    

def register_database(first_name, last_name, document_type, document, gender, adress, state , phone_number , email):
    asociado = Asociado(first_name, last_name, document_type, document, gender, adress, state , phone_number , email)
    asociado.register_asociado_database()        
    return redirect(url_for("gestion_asociados"))  

def eliminar_cuota_asociado(id):
    Cuota.eliminar_cuotas_asociado(id)
    return True


def export_pdf():
    lista_asociados = Asociado.list_asociados()
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    html = render_template('/pdfs/pdf_asociado.html', asociados=lista_asociados)
    pdf = pdfkit.from_string(html,False,configuration=config)
    resp = make_response(pdf)
    resp.headers["Content-Type"] = "aplication/pdf"
    resp.headers["Content-Disposition"] = "inline;filename=asociados.pdf"
    return resp
    

def export_csv():
    return "entro al exportar csv"