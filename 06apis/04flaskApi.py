from flask import Flask, jsonify


app = Flask(__name__)


alumnos = ["Jose Manuel", "Joaquin", "Josue", "Federico"]

mascotas = {
    "nombre": "Tofu",
    "edad": 2,
    "tipo": "Perro"
}


@app.route("/")
def index():
    return '''
        Bienvenido a la API demo 1.0 <hr>
        Endpoints disponibles <hr>
        /api/v1/lista <hr>
        /api/v1/diccionario <hr>
    '''
@app.route("/api/v1/lista")
def lista():
    return jsonify(alumnos)

@app.route("/api/v1/diccionario")
def diccionario():
    return mascotas



if __name__ == "__main__":
    app.run(debug=True)