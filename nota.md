import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCKET TCP
# teste print(client)

client.connect(("google.com", 80)) #conectando no google na porta 80 ao executar não apresentou nenhum erro

#client.send("Oi, tudo bem?") #mandando um dado para o servidor, no entanto, a função .send só envia mensagens em formato de bits, em formato de strings vai apresentar um erro

#client.send(b"Oi, tudo bem?") #passando com o b na frente na string ja resolve o problema anterior

#client.recv(1024) #agora estamos recebendo dados EM BITS do google, mas não iremos receber nada, pq estamos não estamos enviando uma requisição HTTP padrão, mas vamos enviar para descobrir como é uma
