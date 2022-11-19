from unicodedata import category
from src.core.models.asociado_model import Asociado
from flask import render_template, request, redirect , url_for, flash, make_response, Response
from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota
from src.core.models.config_model import Config
from flask import current_app as app
import pdfkit
import io
import xlwt
from src.web.controllers import login_required
from datetime import datetime


@login_required
def crear_asociado():
    if request.method == 'POST':
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
        if verify_format(document, phone_number) and not verify_asociado(document, document_type)and verify_lenghts(first_name, last_name, document, adress, email, phone_number): 
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
            if valor == '' :
                if clave != "phone_number":
                    if clave != "email":
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
        
        if valido:    
            if verify_format(document, phone_number) and verify_lenghts(first_name, last_name, document, adress, email, phone_number) and not verify_asociado_not_actual(id, document, document_type):
                asoc.update_asociado_database(first_name, last_name, document_type, document, gender, adress, phone_number, email)
                return redirect(url_for("gestion_asociados")) 
        # return render_template('/user/modificar_usuario.html', usu=usu) 
        return redirect(url_for("gestion_asociados"))  

@login_required
def inscribir_asociado_disciplina(id):    
    config = Config.get_self(Config, 1)
    page = request.args.get('page', 1, type=int)
    disciplinasActuales = Disciplina.list_disciplinas_activas(page,config.cant)
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
    monto_base = Config.get_valor_cuota()
    if asociado is None:
        flash("el asociado no existe")
        return redirect(url_for("gestion_asociados"))
    if asociado.state == "Activo":
        if Asociado.tiene_disciplina(id_a, id_d):
            flash("Ya esta inscripto en esta disciplina")
        else:
            Asociado.inscribir_disciplina(asociado, disciplina)
            #generar cuotas
            #periodos = [ "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septembre", "Octubre", "Noviembre", "Diciembre"]
            periodos={ 1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio",
             7:"Julio",8: "Agosto", 9:"Septiembre",10: "Octubre", 11:"Noviembre",12:"Diciembre"}
            fecha_hoy = datetime.now()
            mes_actual=int(fecha_hoy.strftime('%m'))
            año_actual=fecha_hoy.strftime('%Y')
<<<<<<< HEAD
            for i in range(mes_actual , 13):
=======
            for i in range(mes_actual, 13):
>>>>>>> development
                cuo = Cuota(asociado.id, disciplina.id, disciplina.monthly_cost + monto_base, periodos.get(i)+ " " + año_actual)
                cuo.register_cuota_database()
    else:
        flash("El usuario al que desea inscribir se encuentra con el estado moroso")
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

def verify_format(document, phone_number):
    try: 
        document = int(document)        
    except ValueError:
        flash("Solo puede ingresar numeros en el documento")
        return False
    return True


def verify_lenghts(first_name, last_name, document, adress, email, phone_number):
    #name
    if len(first_name) == 0:
        flash("Nombre vacio, complete el campo")
        return False
    else:
        if len(first_name) > 30:
            flash("Nombre muy largo")
            return False
        elif len(first_name) < 5:
            flash("Nombre muy corto")
            return False   
    #last_name
    if len(last_name) == 0:
        flash("Apellido vacio, complete el campo")
        return False
    else:
        if len(last_name) > 30:
            flash("Apellido muy largo")
            return False
        elif len(last_name) < 5:
            flash("Apellido muy corto")
            return False            
    #document
    if len(document) == 0:
        flash("Documento vacio, complete el campo")
        return False
    else:
        if len(document) > 15:
            flash("Documento muy largo")
            return False
        elif len(document) < 8:
            flash("Documento muy corto")
            return False 
    #adress
    if len(adress) == 0:
        flash("Direccion vacio, complete el campo")
        return False
    else:
        if len(adress) > 50:
            flash("Direccion muy larga")
            return False
        elif len(adress) < 5:
            flash("Direccion muy corta")
            return False 
    #email
    if len(email) != 0:
        if len(email) > 50:
            flash("Email muy largo")
            return False
        elif len(email) < 15:
            flash("Email muy corto")
            return False 
    #phone_number
    if len(phone_number) != 0:      
        if len(phone_number)!=9:
            flash("El numero de telefono debe ser de 9 digitos")
            return False 
    return True

# def verify_empty(first_name, last_name, document_type, document, gender, adress, state , phone_number , email):
    

def register_database(first_name, last_name, document_type, document, gender, adress, state , phone_number , email):
    asociado = Asociado(first_name, last_name, document_type, document, gender, adress, state , phone_number , email)
    asociado.register_asociado_database()        
    return redirect(url_for("gestion_asociados"))  

def eliminar_cuota_asociado(id):
    Cuota.eliminar_cuotas_asociado(id)
    return True



def export_pdf():
    lista_asociados = Asociado.list_asociados()
    html = render_template('/pdfs/pdf_asociado.html', asociados=lista_asociados)
    if app.config.get("USE_WKHTML_CUSTOM_PATH") == True:
        path_wkhtmltopdf = app.config.get("WKHTML_CUSTOM_PATH")
        config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)    
        pdf = pdfkit.from_string(html,False,configuration=config)
    else:
        pdf =pdfkit.from_string(html,False)
    resp = make_response(pdf)
    resp.headers["Content-Type"] = "aplication/pdf"
    resp.headers["Content-Disposition"] = "inline;filename=asociados.pdf"
    return resp

    

def export_csv():
    '''Exportar un csv'''
    asociados = Asociado.list_asociados()
    
    output = io.BytesIO()
    workbook = xlwt.Workbook()
    #Agregar a la hoja del Csv
    sh = workbook.add_sheet('Lista de asociados')
    
    '''Se crean los nombres de las
        columnas en el csv'''
        
    sh.write(0,0,'Nro de Socio')
    sh.write(0,1,'Apellido')
    sh.write(0,2,'Nombre')
    sh.write(0,3,'Tipo de Documento')
    sh.write(0,4,'Nro Documento')
    sh.write(0,5,'Genero')
    sh.write(0,6,'Email')
    
    #cargar datos del asociado por fila
    indice = 0
    for a in asociados:
        sh.write(indice + 1,0,a.id)
        sh.write(indice + 1,1,a.last_name)
        sh.write(indice + 1,2,a.first_name)
        sh.write(indice + 1,3,a.document_type)
        sh.write(indice + 1,4,a.document)
        sh.write(indice + 1,5,a.gender)
        sh.write(indice + 1,6,a.email)
        indice +=1
    
    workbook.save(output)
    output.seek(0)
    return Response(output, mimetype="application/ms-Excel", headers= {"Content-Disposition":"attachment;filename=Lista de asociados.csv"})

def buscar_usuario_asociado():
    page = request.args.get('page', 1, type=int)
    config = Config.get_self(Config, 1)

    lista_usuario = Asociado.search_by_status(request.args['estado'],page,config.cant)
    results = Asociado.get_paginated(Asociado, lista_usuario, page, config.cant)

    return render_template("gestion_asociados.html", asoc=results)

def carnet_digital(id):
    asociado = Asociado.get_asociado_by_id(id)
    fecha = asociado.get_fecha()
    dia_actual=fecha.strftime('%d')
    mes_actual=fecha.strftime('%m')
    año_actual=fecha.strftime('%Y')
    fecha_ingreso= dia_actual+ "/" + mes_actual +"/"  + año_actual
    return render_template("/asociado/carnet.html", asociado=asociado , fecha = fecha_ingreso)