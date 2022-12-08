#!/usr/bin/env python3

import pygal

def get_status():
    x_time = []
    status = []
    with open('/home/marty/Documents/Admin_redes/Pygal_PySNMP/main/functions/traps.txt','r') as f:
        for line in f.readlines():
            line = eval(line)
            x_time.append(line['Time'])
            status.append(line['Status'])
            line_chart = pygal.Line()
            line_chart.title = "Status"
            line_chart.x_labels = x_time
            line_chart.add('Status',status)
    return line_chart

def graficar():
    x_time = []
    in_packets = []
    with open('/home/marty/Documents/Admin_redes/Pygal_PySNMP/main/functions/resultados.txt', 'r') as f:
        l = eval(f.readline())
        aux = int(l['Fa2-0_In_uPackets'])
        for line in f.readlines():
           line = eval(line)
           x_time.append(line['Tiempo'])
           in_packets.append(int(line['Fa2-0_In_uPackets'])-aux)
           aux = int(line['Fa2-0_In_uPackets'])
           line_chart = pygal.Line()
           line_chart.title = "R1 Fa2/0"
           line_chart.x_labels = x_time
           line_chart.add('Paq. entrada', in_packets)
    return line_chart
