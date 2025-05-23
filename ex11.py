from random import randint

matriz = []
qntd = 0

for i in range(3):
    linha = []
    for j in range(5):
        linha.append(randint(1,50))
    matriz.append(linha)

for i in range(3):
    for j in range(5):
        if 15 <= matriz[i][j] <= 20:
            qntd += 1


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'{matriz[i][j]:4}', end= '')
    print()

print(f'A quantidade de números entre 15 e 20 são: {qntd}')
