from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.engine import Engine

#Datos para la conexiòn a BD

dataBaseName="gestordb"
userName="root"
userPassword=""
connectionPort=3306
server="localhost"

# Creando la conexiòn 

dataBaseConnection = f"mysql+mysqlconnector:// {userName}:{userPassword}@{server}:{connectionPort}/{dataBaseName}"

#Creo el motor de conexión
engine=create_engine(dataBaseConnection)

#Abrir la sesión con la BD
SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)



