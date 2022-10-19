from src.core.models.disciplina_model import Disciplina
from src.core.models.cuota_model import Cuota
from flask import render_template ,request, redirect, url_for ,flash 
from src.web.controllers import login_required

@login_required
def realizar_pago():
    return render_template("pago_de_una_couta/realizar_pago.html") 

