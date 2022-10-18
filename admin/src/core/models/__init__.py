from src.core.database import db
from src.core.models.config_model import Config


def crear_configuracion(**kwargs):
    config = Config(**kwargs)
    db.session.add(config)
    db.session.commit()
    return config
