import nmap

def verificar_hosts(hosts_in):
    nm = nmap.PortScanner()
    nm.scan(hosts=hosts_in, arguments='-T5 --min-rate 5000 -n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    return hosts_list

def verificar_puertos(host_in):
    nm = nmap.PortScanner()
    nm.scan(host_in, arguments='-T5 -open -p1-1023 -n -Pn')
    ports_list = [(x, nm[host_in]['tcp'][x]['state']) for x in nm[host_in]['tcp'].keys()]
    return ports_list

def informacion_puerto(host_in,port_in):
    nm = nmap.PortScanner()
    nm.scan(host_in,port_in)
    if nm[host_in].has_tcp(int(port_in)):
        data = nm[host_in]['tcp'][int(port_in)]
        return data
    else:
        return {"Incorrect":"Port down"}