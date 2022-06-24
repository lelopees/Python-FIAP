from ftplib import * 

ftp =FTP('ftp.ibiblio.org')
print(ftp.getwelcome())

usuario = input("Digite o usuário: ")
senha= input("Digite a senha: ")

ftp.login(usuario, senha)

print("Diretório atual de trabalho: ", ftp.pwd())

ftp.cwd('pub') # diretório que eu quero acessar

print("Diretório corrente: ", ftp.pwd)

print(ftp.retrlines('LIST')) # listar todos os arquivos da pasta

ftp.quit()