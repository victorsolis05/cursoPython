from os import read
import csv

# Engine: controla la conexion a la base de datos
from sqlalchemy import create_engine, engine
# base controla los objetos para el modelo ORM
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
# Session, controla los queries
from sqlalchemy.orm import Session
from sqlalchemy import inspect


#engine = create_engine("sqlite:///wwe.sqlite")
#engine = create_engine("mysql+pymysql://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?charset=utf8")
engine = create_engine("postgresql+psycopg2://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?client_encoding=utf8")

Base = declarative_base()


class Luchador(Base):
    __tablename__ = "luchadores"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30))
    wins = Column(Integer)
    losses = Column(Integer)
    draws = Column(Integer)

if inspect(engine).has_table("luchadores"):
    Luchador.__table__.drop(engine)


# Equivalente a crear la tabla y la base de datos
Base.metadata.create_all(engine)

session = Session(bind=engine)


with open("./data/07WWE-Data-2016.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for x in csvreader:
        a, b, c, d = x
        luchador1 = Luchador(name=a, wins=b, losses=c, draws=d)
        session.add(luchador1)
    session.commit()

# Query a la base de datos

resultados = session.query(Luchador).order_by("name").limit(5).all()
for x in resultados:
    print(x.name)

session.close()
engine.dispose()
