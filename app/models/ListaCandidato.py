import enum

from sqlalchemy import Enum

from app import db
from app import ma

class EstadoListaEnum(enum.Enum):
    aprobado = "aprobado"
    desaprobado = "desaprobado"
    pendiente = "pendiente"

class ListaCandidato(db.Model):
    __tablename__ = 'lista_candidato'
    id_lista = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=True)
    estado = db.Column(Enum(EstadoListaEnum), nullable=True, default=EstadoListaEnum.pendiente)
    id_eleccion = db.Column(db.Integer, db.ForeignKey('eleccion.id_eleccion'), nullable=True)
    propuestas = db.relationship('Propuesta', backref='lista_candidatol', lazy=True)
    candidatos = db.relationship('Candidato', backref='lista_candidatol', lazy=True)

    def __init__(self, nombre, id_eleccion, estado=EstadoListaEnum.pendiente):
        self.nombre = nombre
        self.id_eleccion = id_eleccion
        self.estado = estado
        
class ListaCandidatoSchema(ma.Schema):
    class Meta:
        fields = (
            'id_lista',
            'nombre',
            'estado',
            'id_lista'
        )
