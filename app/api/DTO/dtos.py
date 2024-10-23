from pydantic import BaseModel, Field 
from datetime import date

#los dto son clases que establecen el modelo de transferencia de datos
class UsuarioDTOPeticion(BaseModel):
    nombres:str
    fechaNacimiento:date
    ubicacion:str
    metaAhorro:float
    class Config:
        orm_mode=True

class UsuarioDTORespuesta(BaseModel):
    id:int
    nombres:str
    metaAhorro:float
    class Config:
        orm_mode=True

class GastosDTOPeticion(BaseModel):
    descripcion:str
    categoria:str
    valor:float
    fecha:date
    class Config:
        orm_mode=True    

class GastosDTORespuesta(BaseModel):
    id:int
    valor:float
    fecha:date
    class Config:
        orm_mode=True

class CategoriaDTOPeticion(BaseModel):
    nombre:str
    descripcion:str
    fotoCategoria:str
    class Config:
        orm_mode=True

class CategoriaDTORespuesta(BaseModel):
    id:int
    nombre:str
    descripcion:str
    class Config:
        orm_mode=True

class IngresoDTOPeticion(BaseModel):
    descripcion:str
    valor:float
    fecha:date
    class Config:
        orm_mode=True

class IngresoDTORespuesta(BaseModel):
    id:int
    descripcion:str
    valor:float
    class Config:
        orm_mode=True
