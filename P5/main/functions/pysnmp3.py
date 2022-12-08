#!/usr/bin/python3
from pysnmp.entity.rfc3413.oneliner import cmdgen
import datetime

cmdGen = cmdgen.CommandGenerator()

host = '192.168.0.1'
community = 'secreta'

# Hostname OID
system_name = '1.3.6.1.2.1.1.5.0'

# Interface OID
fa2_0_in_uPackets = '1.3.6.1.2.1.2.2.1.11.4'


def snmp_query(host, community, oid):
    errorIndication, errorStatus, errorIndex, varBinds = cmdGen.getCmd(
        cmdgen.CommunityData(community),
        cmdgen.UdpTransportTarget((host, 161)),
        oid
    )
    
    # Revisamos errores e imprimimos resultados
    if errorIndication:
        print(errorIndication)
    else:
        if errorStatus:
            print('%s at %s' % (
                errorStatus.prettyPrint(),
                errorIndex and varBinds[int(errorIndex)-1] or '?'
                )
            )
        else:
            for name, val in varBinds:
                return(str(val))

result = {}
result['Tiempo'] = datetime.datetime.utcnow().isoformat()
result['Fa2-0_In_uPackets'] = snmp_query(host, community, fa2_0_in_uPackets)

with open('/home/marty/Documents/Admin_redes/Pygal_PySNMP/main/functions/resultados.txt', 'a') as f:
    f.write(str(result))
    f.write('\n')
