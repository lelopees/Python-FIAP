from ast import USub
import platform
import getpass
from datetime import datetime

print("Nome maquina: ...........", platform.node())
print("Arquitetura : ...........", platform.architecture())
print("Sistema Operacional: ....", platform.system())
print("Versão do SO: ...........", platform.release())
print("Processador: ............", platform.processor())
print("Versao do Python: .......", platform.python_version())

print(datetime.now().year)
print(datetime.now().hour)
print(datetime.now().day)
print(datetime.now().minute)

#print(getpass.getuser()) # usuário da maquina
#print(getpass.getpass("Digite sua senha...."))

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha....")
if usuario == 'leticia.lopes' and senha == 'Hello':
    print('Bem-venda Adele')
else:
    print('Você não tem acesso')
