from socket import *

servidor = "127.0.0.1"  # localhost
porta = 43210

# AF_INET tipo de identificação
# SOCK_DGRAM para protocolo udp
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor,porta))
print("Servidor pronto...")

while True:
    dados, origem = obj_socket.recvfrom(65535) #range maximo de portas.
    print("Origem............: ", origem)
    print("Dados recebidos...:", dados.decode())
    resposta = input("Digite a resposta: ")
    # encode para enviar a resposta em bytes
    obj_socket.sendto(resposta.encode(), origem) 

obj_socket.close()


