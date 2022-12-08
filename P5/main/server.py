
from flask import Flask, url_for, jsonify, request
from functions.pygal2 import get_status, graficar
import os
import time

app = Flask(__name__)

class ValidaError(ValueError):
    pass

from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(2)
executor2 = ThreadPoolExecutor(2)

@app.route('/monitoreo')
def iniciar_monitoreo():
    executor.submit(monitoreo_paquetes)
    executor2.submit(traps)
    return jsonify({'Correcto':'Monitoreo incializado'})

def monitoreo_paquetes():
    for i in range(36):
        os.system("python3 /home/marty/Documents/Admin_redes/Pygal_PySNMP/main/functions/pysnmp3.py")
        time.sleep(5)

def traps():
    os.system("python3 /home/marty/Documents/Admin_redes/Pygal_PySNMP/main/functions/trampas.py")

@app.route('/grafica/paquetes', methods=['GET'])
def generar_grafica1():
    chart = graficar()
    return chart.render_response()

@app.route('/grafica/status', methods=['GET'])
def generar_grafica2():
    chart = get_status()
    return chart.render_response()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




