#Engine: controla la conexion a la base de datos
from sqlalchemy import create_engine, engine
#base controla los objetos para el modelo ORM
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
#Session, controla los queries
from sqlalchemy.orm import Session

#Conexión a la base de datos

#engine = create_engine("sqlite:///mascotas.db")
#engine = create_engine("postgresql+psycopg2://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?client_encoding=utf8")
engine = create_engine("mysql+pymysql://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?charset=utf8")
#Después de haber hecho el engina, todo el código deberia funcionar
#para cualquier tipo de base de datos
#Vamos a construir manualmete nuestro objeto
Base = declarative_base()
class Persona(Base):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    has_pet = Column(Boolean)
    pet_type = Column(String(30))
    pet_name = Column(String(30))
    pet_age = Column(Integer)

Persona.__table__.drop(engine)

persona1 = Persona(name="manuel", has_pet =True, pet_type="Perro", pet_name="Milaneso", pet_age = 4)
persona2 = Persona(name="luis", has_pet =True, pet_type="Perro", pet_name="Dali", pet_age = 8) 

#Equivalente a crear la tabla y la base de datos
Base.metadata.create_all(engine)

session = Session(bind=engine)

session.add(persona1)
session.add(persona2)

session.commit()

#Query a la base de datos

resultados = session.query(Persona)
for x in resultados:
    print(x.name)

session.close()
engine.dispose()