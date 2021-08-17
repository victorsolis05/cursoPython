from os import read
import csv

# Engine: controla la conexion a la base de datos
from sqlalchemy import create_engine, engine
# base controla los objetos para el modelo ORM
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,  func
# Session, controla los queries
from sqlalchemy.orm import Session
from sqlalchemy import inspect


#engine = create_engine("sqlite:///wwe.sqlite")
#engine = create_engine("mysql+pymysql://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?charset=utf8")
engine = create_engine("postgresql+psycopg2://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?client_encoding=utf8")

Base = declarative_base()


class Voto(Base):
    __tablename__ = "votos"
    id = Column(Integer, primary_key=True, autoincrement=False)
    county = Column(String(30))
    candidate = Column(String(30))

if inspect(engine).has_table("votos"):
    Voto.__table__.drop(engine)


# Equivalente a crear la tabla y la base de datos
Base.metadata.create_all(engine)

session = Session(bind=engine)


with open("./data/election_data.txt") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        voterID, county, candidate = row
        vote = Voto(id=voterID, county=county, candidate=candidate)
        session.add(vote)
    session.commit()

# Query a la base de datos

resultados = session.query(Voto.candidate, func.count(Voto.id)).group_by(Voto.candidate).all()
for x in resultados:
    print(x.name)

session.close()
engine.dispose()
