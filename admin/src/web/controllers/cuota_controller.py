from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota
from src.core.models.asociado_model import Asociado
from flask import render_template ,request, redirect, url_for ,flash 
from src.web.controllers import login_required

@login_required
def realizar_pago():
    cuota_actual = Cuota.list_cuota()
    disciplina_actual = Disciplina.list_disciplina()
    asociado_actual = Asociado.list_asociados()
    print(cuota_actual)
    print(disciplina_actual)
    print( asociado_actual)
    return render_template("pago_de_una_couta/realizar_pago.html") 

