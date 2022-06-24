from socket import *

servidor = "127.0.0.1"  # localhost
porta = 43210

# AF_INET tipo de identificação
# SOCK_DGRAM para protocolo udp
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor,porta))
saida=""

while saida!="X":
    msg = input("Sua mensagem:  ")
    obj_socket.sendto(msg.encode(), (servidor, porta))
    dados, origem = obj_socket.recvfrom(65535)  # range maximo de portas.
    print("Respostas do servidor: ", dados.decode())
    saida=input("Digite <X> para sair: ").upper()

obj_socket.close()
