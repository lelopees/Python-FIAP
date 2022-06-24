from ftplib import *

ftp = FTP('ftp.ibiblio.org') # dominio aberto, para teste

print(ftp.getwelcome())

ftp.quit()