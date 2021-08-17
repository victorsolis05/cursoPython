#Hacer un único código que funcione con cualquier motor de base de datos
#ORM - Basado en Objetos
#SQLAlchemy

#en SQLALchemy, tenemos 3 objetos muy importantes: engine, base y session.

#Engine: Controla la conexión a la base de datos
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://cursoPython:12345678@LAPTOP-7RNEL8E4/postgres?client_encoding=utf8")
#engine = create_engine("mysql+pymysql://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?charset=utf8")
#engine = create_engine("sqllite:///miPrimerBase.db")

# "postgresql+pyscopg2://"
# "mysql+pymsql://root@localhost:3660/cursoPython"

resultados = engine.execute("select * from people")

[print(x) for x in resultados]


