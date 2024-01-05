from flask import Flask, url_for, jsonify, request
from pynmap import verificar_hosts, verificar_puertos, informacion_puerto

app = Flask(__name__)

class ValidaError(ValueError):
    pass

@app.route('/')
def bienvenida():
    return jsonify({'Hola':'Hola'})

@app.route('/escanear-puertos', methods=['POST'])
def escanear_puertos():
    data = request.json
    res = verificar_puertos(data['Host'])
    return jsonify(res)

@app.route('/escanear-hosts', methods=['POST'])
def escanear_subred():
    data = request.json
    res = verificar_hosts(data['Hosts'])
    return jsonify(res)

@app.route('/escanear-puerto', methods=['POST'])
def obtener_puerto():
    data = request.json
    res = informacion_puerto(data['Host'],data['Port'])
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)