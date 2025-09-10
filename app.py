from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

@app.route("/acerca_de")
def about():
    return "Ayudame senior a hacer la app de bromato ya con este lenguaje jeje"

@app.route("/api/info")

def api_info():
    data= {
        "Nombre": "App de Notas",
        "Version": "0.1.1"
    }
    return jsonify(data),200

if __name__ == "__main__":
    app.run(debug=True)