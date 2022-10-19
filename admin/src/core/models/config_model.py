from datetime import datetime
from src.core.database import db

class Config(db.Model):
    
    __tablename__ = 'config'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    cant = db.Column(db.Integer)
    estado_pagos = db.Column(db.Integer)    
    info_contacto = db.Column(db.String(128))    
    texto_encabezado = db.Column(db.String(128))    
    valor_cuota = db.Column(db.Integer)    
    recargo_cuota = db.Column(db.Integer)
    
    inserted_at = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now)
    created_at = db.Column(db.DateTime, default=datetime.now())


    def __init__(self, cant=None, estado_pagos=None, info_contacto=None,texto_encabezado=None, valor_cuota=None, recargo_cuota=None):
        self.cant = ((cant),)
        self.estado_pagos = ((estado_pagos),)
        self.info_contacto = ((info_contacto),)
        self.texto_encabezado = ((texto_encabezado),)
        self.valor_cuota = ((valor_cuota),)
        self.recargo_cuota = ((recargo_cuota),)


    def get_configuration():
        return Config.query.order_by(Config.id.desc()).first()

    def get_page_rows():
        return Config.get_configuration().page_size

    def get_self(self, disip_id):
        return Config.query.filter(self.id == disip_id).first()    

    def update_config_database(self, cant, estado_pagos, info_contacto, texto_encabezado, valor_cuota, recargo_cuota ):
        self.cant = cant
        self.estado_pagos = estado_pagos
        self.info_contacto = info_contacto
        self.texto_encabezado = texto_encabezado
        self.valor_cuota = valor_cuota
        self.recargo_cuota = recargo_cuota
        db.session.commit()
