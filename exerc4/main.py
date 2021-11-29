#Faça um Programa que peça duas notas de 5 alunos, 
# calcule e armazene num vetor a média de cada aluno,
#  imprima o número de alunos com média maior ou igual a 7.0.

def notas_est_vet():
    acima_media = 0
    media = []
    for alunos in range(5):
        notas = 0
        for nota in range(2):
            print(f"digite a nota {nota +1} do aluno {alunos + 1} ")
            notas += int(input())

        media.append(notas/2)
        if media[alunos] >= 7.0:
            acima_media += 1
    print(f'Médias acima de 7: {acima_media}')


notas_est_vet()