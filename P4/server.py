
from flask import Flask, url_for, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
from paramiko_1 import activate_ospf, activate_rip, activate_static
from reset import disable_ospf, disable_rip, disable_static

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/marty/Documents/Admin_redes/databases/enrutamiento_multiple.db'
bd = SQLAlchemy(app)

class ValidaError(ValueError):
    pass

class Enrutamiento(bd.Model):
    __tablename__ = 'enrutamiento'
    id = bd.Column(bd.Integer, primary_key=True)
    protocolo = bd.Column(bd.String(120), index=True)
    ip = bd.Column(bd.String(20), index=True)
    id_red = bd.Column(bd.String(20), index=True)
    mask = bd.Column(bd.String(20),index=True)
    jump = bd.Column(bd.String(20),index=True,nullable=True)

    def dame_url(dis):
        return url_for('dame_enrutamiento', id=dis.id, _external=True)

    def exporta_datos(dis):
        return {
            'url': dis.dame_url(),
            'protocolo': dis.protocolo,
            'id_red': dis.id_red,
            'mask': dis.mask,
            'jump': dis.jump,
            'msg': 'Protocolo levantado'
        }

    def get_datos(dis):
       return dis.protocolo, dis.ip, dis.id_red, dis.mask, dis.jump

@app.route('/enrutamientos/', methods=['GET'])
def dame_enrutamientos():
    return jsonify({'enrutamiento': [enrutamiento.dame_url()
                               for enrutamiento in Enrutamiento.query.all()]})

@app.route('/enrutamientos/<int:id>', methods=['GET'])
def dame_enrutamiento(id):
    protocolo, ip, id_red, mask, jump = Enrutamiento.query.get_or_404(id).get_datos()
    if protocolo == 'ospf':
         activate_ospf(ip,id_red,mask)
    elif protocolo == 'rip':
         activate_rip(ip,id_red)
    else:
         activate_static(ip,id_red,mask,jump)
    return jsonify(Enrutamiento.query.get_or_404(id).exporta_datos())

@app.route('/enrutamientos/todos', methods=['GET'])
def levanta_enrutamientos():
    protocolo, ip, id_red, mask, jump = Enrutamiento.query.get_or_404(1).get_datos()
    activate_ospf(ip,id_red,mask)
    protocolo, ip, id_red, mask, jump = Enrutamiento.query.get_or_404(3).get_datos()
    activate_rip(ip,id_red)
    protocolo, ip, id_red, mask, jump = Enrutamiento.query.get_or_404(2).get_datos()
    activate_static(ip,id_red,mask,jump)
    return jsonify({'Correcto':'Protocolos de enrutamiento levantados'})

@app.route('/enrutamientos/todos', methods=['DELETE'])
def desactiva_enrutamientos():
    protocolo, ip, id_red, mask, jump = Enrutamiento.query.get_or_404(1).get_datos()
    disable_ospf(ip,id_red,mask)
    protocolo, ip, id_red, mask, jump = Enrutamiento.query.get_or_404(3).get_datos()
    disable_rip(ip,id_red)
    protocolo, ip, id_red, mask, jump = Enrutamiento.query.get_or_404(2).get_datos()
    disable_static(ip,id_red,mask,jump)
    return jsonify({'Correcto':'Protocolos de enrutamiento desactivados'})

if __name__ == '__main__':
    bd.create_all()
    app.run(host='0.0.0.0', debug=True)




