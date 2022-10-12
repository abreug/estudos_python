import socket

#trazendo informações do google atraves de uma requisição HTTP

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("google.com", 80))
client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n")
pacotes_recebidos = client.recv(1024).decode()
print(pacotes_recebidos)