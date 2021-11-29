#Faça um Programa que leia 4 notas de alunos e, 
# ao final, mostre na tela as notas lidas e a respectiva média

nota1 =float(input('digite a primeira nota' )) 
nota2 = float (input('digite a segunda nota' ))
nota3 = float (input('digite a terceira nota' ))
nota4 = float (input('digite a quarta nota' ))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'As notas foram {nota1}, {nota2}, {nota3}, {nota4}, e a média é {media}')