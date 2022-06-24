with open('pagina.html', 'w') as pagina:
    #body indica o inicio do con´teudo
    #h1 maior para titulos
    pagina.write('<body> <h1> Esta é um teste para página web </h1>')
    #h2 uma fonte menor que h1
    #br para quebra de linha
    pagina.write('<br><h2> Abaixo seguem nomes importante para o projeto </h2>')
    #h3 uma fonte menor que h2 
    pagina.write('<h3>')
    nome= ''
    while nome!='SAIR':
        nome = input("Digite um nome ou SAIR karen").upper()
        if nome!="SAIR":
            pagina.write('<br>'+nome)
    pagina.write('</h3></body>')