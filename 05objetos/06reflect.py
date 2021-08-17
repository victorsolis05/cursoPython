from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


#engine = create_engine("sqlite:///wwe.sqlite")
#engine = create_engine("mysql+pymysql://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?charset=utf8")
engine = create_engine("postgresql+psycopg2://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?client_encoding=utf8")
Base = automap_base()
Base.prepare(engine, reflect = True)
#SOLO FUNCIONA SI LA TABLA TIENE LLAVE PRIMARIA o INDICES
Luchador = Base.classes.luchadores
session = Session(bind=engine)


resultados = session.query(Luchador.name, Luchador.wins).order_by("name").limit(5).all()
for x in resultados:
    print(x.name)


results = (
    session
    .query(Luchador.name, Luchador.wins)
    .filter(Luchador.wins > 50)
    .order_by(Luchador.wins.desc())
    .limit(5)
    .all()
)

print(results)

session.close()
engine.dispose()