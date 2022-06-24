from email.mime import base

basedados = []

with open("iris.data", "r") as arquivo:
    for registro in arquivo.readlines():
        basedados.append(registro.split(","))
    
#print(basedados)

#print('Total = ' + str(float(basedados[0][0]) + float(basedados[0][1]) +
      #float(basedados[0][2]) + float(basedados[0][3])) + ' ' + basedados[0][4])

#print('Total = ' + str(float(basedados[1][0]) + float(basedados[1][1]) +
      #float(basedados[1][2]) + float(basedados[1][3])) + ' ' + basedados[1][4])

for p1, p2, p3, p4, p5 in basedados: 
    total = float(p1) + float(p2) + float(p3) + float(p4)
    print('{} valores {} - {} - {} - {} o total é de {}'. format(p5,p1,p2,p3,p4, total))
    

    
 
