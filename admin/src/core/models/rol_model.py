from src.core.database import db
from src.core.models.permiso_model import Permiso


permisos = db.Table('rol_tiene_permiso',
    db.Column('rol_id', db.Integer, db.ForeignKey('rol.id'), primary_key=True),
    db.Column('permiso_id', db.Integer, db.ForeignKey('permiso.id'), primary_key=True)
    
)

class Rol(db.Model):
	__tablename__= 'rol'
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(40))
	#permisos = db.relationship('Permiso', secondary=permisos, backref=db.backref('roles_con_el_permiso', lazy = True), lazy='subquery')
	permisos = db.relationship('Permiso', secondary=permisos, backref=db.backref('roles_con_el_permiso', lazy = False), lazy='dynamic')
	
	@classmethod
	def get_rol_Socio(self):
		return Rol.query.filter(self.nombre == "Socio").first()

	def __init__(
				self, nombre
		):
			self.nombre = nombre

	def __repr__(self):
		return f'Rol(nombre={self.nombre}'

	

	@classmethod
	def tiene_permiso(self,rol,permiso):
		rol= self.obtener_rol(rol)
		return bool(rol.permisos.filter_by(nombre=permiso).first())
  
	@classmethod
	def obtener_rol(self, nombre_rol):
		return Rol.query.filter(self.nombre == nombre_rol).first()
