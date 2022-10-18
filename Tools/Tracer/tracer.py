import socket
import sys


def scan(host, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.5) #atenção caso esteja hospedado em outros paises, pode alterar o tempo de resposta e o cronometro vai atrapalhar ao inves de ajudar
            code = client.connect_ex((host, int(port)))
            #executar, se retornar 0, a porta está aberta, se diferente disso, está fechada.
            if code == 0:
                print("[+] {} open".format(port))
    except:
        print("Error, something is wrong")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        host = sys.arqv[1]
        if len(sys.srgv) >= 3:
            ports = sys.argv[2].split(",")
        else:
            ports = [21, 22, 23, 25, 80, 443, 8080, 3306, 139, 135] #principais portas

        scan(host, ports)    
    else:
        print("Usage: python tracer.py google.com 22,23,80,3306")