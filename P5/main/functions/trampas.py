#Receptor python de traps snmp
from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dgram import udp
from pysnmp.entity.rfc3413 import ntfrcv
import logging
import datetime

snmpEngine = engine.SnmpEngine()

TrapAgentAddress='192.168.0.10'; #Direccion del escucha de traps
Port=162;  #Puerto

config.addTransport(
    snmpEngine,
    udp.domainName + (1,),
    udp.UdpTransport().openServerMode((TrapAgentAddress, Port))
)

#Configuracion de comunidad V1 y V2c
config.addV1System(snmpEngine, 'todo', 'secreta')

def cbFun(snmpEngine, stateReference, contextEngineId, contextName,
          varBinds, cbCtx):
    traps = {}
    val = str((varBinds.pop())[-1])
    traps['Time'] = datetime.datetime.utcnow().isoformat()
    if(val == 'administratively down'):
        traps['Status'] = 0
    else:
        traps['Status'] = 1
    with open('/home/marty/Documents/Admin_redes/Pygal_PySNMP/main/functions/traps.txt','a') as f:
        f.write(str(traps))
        f.write('\n')
        f.close()

ntfrcv.NotificationReceiver(snmpEngine, cbFun)

snmpEngine.transportDispatcher.jobStarted(1)

try:
    snmpEngine.transportDispatcher.runDispatcher()
except:
    snmpEngine.transportDispatcher.closeDispatcher()
    raise