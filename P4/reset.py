#!/usr/bin/python3

import paramiko, time

def disable_ospf(ip, id_red, mask):
    conexion = paramiko.SSHClient()
    conexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conexion.connect(ip, username='admin', password='admin', look_for_keys=False, allow_agent=False)
    nueva_conexion = conexion.invoke_shell()
    nueva_conexion.send("conf t\n")
    nueva_conexion.send("router ospf 1\n")
    nueva_conexion.send("redistribute rip subnets\n")
    nueva_conexion.send("redistribute static subnets\n")
    nueva_conexion.send("no network "+id_red+" "+mask+" area 0\n")
    nueva_conexion.close()

def disable_static(ip, id_red, mask, jump):
    conexion = paramiko.SSHClient()
    conexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conexion.connect(ip, username='admin', password='admin', look_for_keys=False, allow_agent=False)
    nueva_conexion = conexion.invoke_shell()
    nueva_conexion.send("conf t\n")
    nueva_conexion.send("no ip route "+id_red+" "+mask+" "+jump+"\n")
    nueva_conexion.close()

def disable_rip(ip, id_red):
    conexion = paramiko.SSHClient()
    conexion.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    conexion.connect(ip, username='admin', password='admin', look_for_keys=False, allow_agent=False)
    nueva_conexion = conexion.invoke_shell()
    nueva_conexion.send("conf t\n")
    nueva_conexion.send("router rip\n")
    nueva_conexion.send("version 2\n")
    nueva_conexion.send("redistribute ospf 1 metric 1\n")
    nueva_conexion.send("redistribute static\n")
    nueva_conexion.send("no network "+id_red+"\n")
    nueva_conexion.close()