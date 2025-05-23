from random import randint

linhas = 6
colunas = 3

matriz = []



for i in range(linhas):
    valores = []
    for j in range(colunas):
        valores.append(randint (1, 50))
    matriz.append(valores)

maior_valor = 0
posicao_maior = (0, 0)
menor_valor = matriz[0][0]
posicao_menor = (0, 0)

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]       
            posicao_maior = (i, j)
            
        if matriz[i][j] < menor_valor:
            menor_valor = matriz[i][j]          
            posicao_menor = (i, j)


for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz[i][j]:4}', end= '')
    print()

print()
# Lembrando que no python começa do [0][0], antes eu tava adicionando pra ficar igual matematicamente, como a primeira linha e coluna seria [1][1]
print(f'Maior valor: {maior_valor}\nPosição do maior valor: {posicao_maior}') 
print(f'Menor valor: {menor_valor}\nPosição do menor valor:  {posicao_menor}') # a primeira linha e coluna no python é [0][0] na mat é [1][1]
