from random import randint

linhas = 2 
colunas = 4

matriz = []
qntd = 0
qntd_par = 0
soma_par = 0 

for i in range(2):
    linha = []
    for j in range(4):
        linha.append(randint(1,50))
    matriz.append(linha)

for i in range(2):
    for j in range(4):
        if 12 <= matriz[i][j] <= 20:
            qntd += 1
        if matriz[i][j] % 2 == 0:
            qntd_par += 1
            soma_par += matriz[i][j]
            media_par = soma_par / qntd_par


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'{matriz[i][j]:4}', end= '')
    print()

print(f'\nA quantidade de números entre 12 e 20 é: {qntd}\nE a média dos elementos pares da matriz é: {media_par:.2f}')
