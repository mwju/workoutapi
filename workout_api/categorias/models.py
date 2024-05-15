from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from workout_api.contrib.models import BaseModel

class CategoriaModel(BaseModel):
    __tablename__ = 'categorias'

    pk_id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique=True, nullable=False)
    atleta = relationship("AtletaModel", back_populates="categoria")
