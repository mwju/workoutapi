from pydantic import BaseModel

class AtletaResponse(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str
