import socket

#tempo para estabelecer a conexão
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

#trazendo informações do google atraves de uma requisição HTTP
try:
    client.connect(("127.0.0.1", 4466))
    client.send(b"DEU BOM")
    pacotes_recebidos = client.recv(1024).decode()
    print(pacotes_recebidos)
except:
    print("Um erro ocorreu")