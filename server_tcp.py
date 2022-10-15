import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server.bind(("0.0.0.0", 1133))
    server.listen(5)                #numero de conexões simultânea
    print("Listening...")
    server.accept()                 #espera a conexão de um cliente
    server.close()

except Exception as error:
    print("Erro: ", error)
    server.close()