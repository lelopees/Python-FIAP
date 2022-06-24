from socket import *

servidor = "127.0.0.1"  # localhost
porta = 43210

msg = bytes(input("Digite algo: "), 'uft-8')
# AF_INET tipo de identificação
# SOCK_STREAM para protocolo tcp
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.connect((servidor, porta))
obj_socket.send(msg)

resposta = obj_socket.recv(1024) # resposta de 1024bytes
print("Recebemos: ", resposta)
obj_socket.close()

