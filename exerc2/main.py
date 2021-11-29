#Faça um Programa que leia uma string e diga quantas
#  consoantes foram lidas. Imprima as consoantes. 

def checar_consoante(palavra, vogais):
    final = [each for each in palavra if each not in vogais]
    print(len(final))
    print(final)


palavra = input ("Digite uma palavra: ")
vogais = "AaEeIiOoUu"
checar_consoante(palavra, vogais)