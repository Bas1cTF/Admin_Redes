from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crea una aplicación Flask, carga la configuración
# y crea el objeto SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/marty/Documents/Admin_redes/databases/enrutamiento_multiple.db'
bd = SQLAlchemy(app)

# This is the database model object
class Dispositivo(bd.Model):
    __tablename__ = 'enrutamiento'
    id = bd.Column(bd.Integer, primary_key=True)
    protocolo = bd.Column(bd.String(120), index=True)
    ip = bd.Column(bd.String(20), index=True)
    id_red = bd.Column(bd.String(20), index=True)
    mask = bd.Column(bd.String(20),index=True)
    jump = bd.Column(bd.String(20),index=True,nullable=True)


    def __init__(self, protocolo, ip, id_red, mask, jump):
        self.protocolo = protocolo
        self.ip = ip
        self.id_red = id_red
        self.mask = mask
        self.jump = jump

    def __repr__(self):
        return '<Dispositivo %r>' % self.hostname


if __name__ == '__main__':
    bd.create_all()
    R1 = Dispositivo('ospf', '10.0.1.254','10.0.4.0','0.0.0.255','')
    R2 = Dispositivo('estatico', '10.0.1.254','10.0.5.0','255.255.255.0','10.0.2.253')
    R3 = Dispositivo('rip', '10.0.1.254','10.0.3.0','','')
    bd.session.add(R1)
    bd.session.add(R2)
    bd.session.add(R3)
    bd.session.commit()
