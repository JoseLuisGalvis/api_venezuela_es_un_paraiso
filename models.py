from pydantic import BaseModel
from typing import List

class SitioTuristico(BaseModel):
    id: int
    nombre: str
    ubicacion: str
    clasificacion: str
    atractivo: str  
    imagen: str     
    caracteristicas: List[str]
