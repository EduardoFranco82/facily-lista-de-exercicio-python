#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#  Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.

print('Digite 20 numeros')
numeros = [int(input("Número: ")) for i in range(20)]

impar = []
par = []
for i in numeros:
    if i % 2 == 0 :
        par.append(i)
    else:
        impar.append(i)
  

print (f'os numeros digitados foram {numeros}')
print (f'os numeros pares foram {par}')
print (f'os numeros impares foram {impar}')