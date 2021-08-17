from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "Hello Mundo"

@app.route("/about")
def about():
    return f'''
        <h1>Hola, esto es about</h1>
        <hr>
        <ul>
            <li>Esta es la pagina de about</li>
        </ul>
    '''
@app.route("/api")
def api():
    return {"usuario": "45079303"}

if __name__ == "__main__":
    app.run(debug=True)