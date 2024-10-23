from fastapi import APIRouter, HTTPException 
from sqlalchemy.orm import Session
from typing import List
from fastapi.params import Depends

from app.api.DTO.dtos import UsuarioDTOPeticion, UsuarioDTORespuesta
from app.api.DTO.dtos import GastosDTOPeticion, GastosDTORespuesta
from app.api.DTO.dtos import CategoriaDTOPeticion, CategoriaDTORespuesta
from app.api.DTO.dtos import IngresoDTOPeticion, IngresoDTORespuesta
from app.api.models.tablasSQL import Usuario
from app.api.models.tablasSQL import Gastos
from app.api.models.tablasSQL import Categoria
from app.api.models.tablasSQL import Ingreso
from app.database.configuration import SessionLocal, engine

rutas = APIRouter()

def conectarConBD():
    try:
        baseDatos= SessionLocal()
        yield baseDatos

    except Exception as error:
        baseDatos.rollback()
        raise error

    finally:
        baseDatos.close()

#Construyendo nuestros servicios

#Cada servicio (Operaciòn o transaccion en BD) debe programarse como una funcion
    #USUARIOS
@rutas.post("/usuario", response_model=UsuarioDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarUsuario (datosUsuario:UsuarioDTOPeticion, database: Session=Depends(conectarConBD)):
    try:
        usuario=Usuario(
            nombres=datosUsuario.nombres,
            fechaNacimiento=datosUsuario.fechaNacimiento,
            ubicacion=datosUsuario.ubicacion,
            metaAhorro=datosUsuario.metaAhorro
        )
        #Ordenandole a la BD
        database.add(usuario)
        database.commit()
        database.refresh(usuario)
        return usuario
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, defail=f"Tenemos un problema {error}")
    
@rutas.get("/usuario", response_model=List[UsuarioDTORespuesta], summary="Buscar todos los usuarios de BD")    
def buscarUsuarios(database: Session=Depends(conectarConBD)):
    try:
        usuarios=database.query(Usuario).all()
        return usuarios    
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, defail=f"No se pueden buscar los usuarios {error}")
    

       #GASTOS
@rutas.post("/gastos", response_model=GastosDTORespuesta, summary="Registrar gastos de la base de datos")
def guardarGastos (datosGastos:GastosDTOPeticion, database: Session=Depends(conectarConBD)):
    try:
        gastos=Gastos(
            descripcion=datosGastos.descripcion,
            categoria=datosGastos.categoria,
            valor=datosGastos.valor,
            fecha=datosGastos.fecha
        )
        #Ordenandole a la BD
        database.add(gastos)
        database.commit()
        database.refresh(gastos)
        return gastos
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, defail=f"Tenemos un problema {error}")

@rutas.get("/gastos", response_model=List[GastosDTORespuesta], summary="Buscar todos los gastos de la BD" )
def buscarGastos(database: Session=Depends(conectarConBD)):
    try:
        gastos=database.query(Gastos).all()
        return gastos
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, defail=f"No se pueden buscar los gastos {error}")
    
    #CATEGORIA
@rutas.post("/categoria", response_model=CategoriaDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarCategoria (datosCategoria:CategoriaDTOPeticion, database: Session=Depends(conectarConBD)):
    try:
        categoria=Categoria(
            nombre=datosCategoria.nombre,
            descripcion=datosCategoria.descripcion,
            fotoCategoria=datosCategoria.fotoCategoria
        )
        #Ordenandole a la BD
        database.add(categoria)
        database.commit()
        database.refresh(categoria)
        return categoria
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, defail=f"Tenemos un problema {error}")
    
@rutas.get("/categoria", response_model=List[CategoriaDTORespuesta], summary="Buscar todos los gastos de la BD" )
def buscarCategoria(database: Session=Depends(conectarConBD)):
    try:
        Categoria=database.query(Categoria).all()
        return Categoria
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, defail=f"No se pueden buscar los gastos {error}")
    
        #INGRESO
@rutas.post("/ingreso", response_model=IngresoDTORespuesta, summary="Registrar un usuario en la base de datos")
def guardarIngreso (datosIngreso:IngresoDTOPeticion, database: Session=Depends(conectarConBD)):
    try:
        ingreso=Ingreso(
           descripcion=datosIngreso.descripcion,
           valor=datosIngreso.valor,
           fecha=datosIngreso.fecha
        )
        #Ordenandole a la BD
        database.add(ingreso)
        database.commit()
        database.refresh(ingreso)
        return ingreso
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, defail=f"Tenemos un problema {error}")
    
@rutas.get("/ingreso", response_model=List[IngresoDTORespuesta], summary="Buscar todos los usuarios de BD")    
def buscarIngreso(database: Session=Depends(conectarConBD)):
    try:
        Ingreso=database.query(Ingreso).all()
        return Ingreso  
    except Exception as error:
        database.rollback()
        raise HTTPException(status_code=400, defail=f"No se pueden buscar los usuarios {error}")