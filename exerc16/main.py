''' Numa eleição existem três candidatos. 
Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''


c1 = 0
c2 = 0
c3 = 0
eleitores = int(input("número de eleitores"))
for n in range(eleitores):
    voto = int(input("vote em 1, 2, ou 3: "))
    if (voto == 1):
        c1 = c1 + 1
    elif (voto == 2):
        c2 = c2 + 1
    elif (voto == 3):
        c3 = c3 + 1
    else:
        print("voto inválido")
print("candidato 1 teve {} votos".format(c1))
print("candidato 2 teve {} votos".format(c2))
print("candidato 3 teve {} votos".format(c3))

