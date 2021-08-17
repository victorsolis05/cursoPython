from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session


# Setip de la base de datos

engine = create_engine(
    "postgresql+psycopg2://cursoPython:12345678@LAPTOP-7RNEL8E4/cursoPython?client_encoding=utf8")
Base = automap_base()
Base.prepare(engine, reflect=True)
Luchador = Base.classes.luchadores


# session = Session(bind=engine)
# resultados = session.query(Luchador.name, Luchador.wins).order_by("name").limit(5).all()
# print(resultados)

# Setup de Flask

app = Flask(__name__)
# Definimos nuestras rutas


@app.route("/")
def index():
    return '''
        <h1>Api de luchadores</h1>
        <hr>
        <p>Indice:</p>
        <ul>
            <li><a href="/api/v1/top5">/api/v1/top5</li>
            <li><a href="/api/v1/peores5">/api/v1/peores5</li>
        </ul>
    '''


@app.route("/api/v1/top5", methods=["GET", "POST"])
def top5():
    session = Session(bind=engine)
    resultados = session.query(Luchador.name, Luchador.wins).order_by(
        Luchador.wins.desc()).limit(5).all()
    session.close()
    lista_resultados = [{"nombre": nombre, "wins": wins}
        for nombre, wins in resultados]
    return jsonify(lista_resultados)


@app.route("/api/v1/peores5")
def peores5():
    session = Session(bind=engine)
    resultados = session.query(Luchador.name, Luchador.losses).order_by(
        Luchador.losses.desc()).limit(5).all()
    session.close()
    lista_resultados = [{"nombre": nombre, "losses": losses}
        for nombre, losses in resultados]
    return jsonify(lista_resultados)


@app.route("/api/v1/<nombre>")
def buscarLuchador(nombre):
    session = Session(bind=engine)
    resultado = session.query(Luchador.name, Luchador.wins).filter(
        Luchador.name == nombre).first()
    session.close()
    print(resultado)
    return jsonify(dict(resultado))


if __name__ == "__main__":
    app.run(debug=True)
