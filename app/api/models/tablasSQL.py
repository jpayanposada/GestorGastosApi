from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey

from sqlalchemy.orm import relationship 

from sqlalchemy.ext.declarative import declarative_base

#Llamado a base para crear tablas
Base=declarative_base()

#Definición de las tablas de mi modelo

#USUARIO
class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    fechaNacimiento=Column(Date)
    ubicacion=Column(String(100))
    metaAhorro=Column(Float)

class Gastos(Base):
    __tablename__ = 'gastos'
    id= Column(Integer, primary_key=True, autoincrement=True)
    descripcion=Column(String(100))
    categoria=Column(String(50))
    valor=Column(Integer)
    fecha=Column(Date)

class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    descripcion=Column(String(100))
    fotoCategoria=Column(String(200))

class Ingreso(Base):
    __tablename__ = 'ingreso'
    id=Column(Integer, primary_key=True, autoincrement=True)
    valor=Column(Integer)
    descripcion=Column(String(100))
    fecha=Column(Date)

