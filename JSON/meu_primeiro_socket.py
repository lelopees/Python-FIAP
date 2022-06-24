import socket

resp = 'S'

while (resp=='S'):
    url = input('Digite uma url:')
    ip=socket.gethostbyname(url)
    print('Do IP referente a url informada é: ', ip)
    resp=input('Digite <s> para continuar').upper()


#g1.globo.com
#www.fiap.com.br
