
matriz1 = []


linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))

#Preencher a matriz. (Nessa opção o usuário deverá definir o tamanho da matriz e a popular.
if linhas < 0 and colunas < 0:
    print('Número inválido.')
else:
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f'Digite o o valor para linha {i} e coluna {j}: ')))
        matriz1.append(linha)

    
#Exibir a matriz formatada na tela (desing de matriz, linha x coluna).
for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz1[i][j]:7}', end= '')
    print()


#Calcular e mostrar a soma de todos os elementos da matriz;
soma = 0
for i in range(linhas):
    for j in range(colunas):
        soma += matriz1[i][j]
print(f'A soma de todos os elementos da matriz é: {soma:.2f}')

print()

#Calcular e mostrar o maior e o menor elemento da matriz, e também suas respectivas posições.
maior_valor = 0
menor_valor = matriz1[0][0]
posicao_maior = (0, 0)
posicao_menor = (0, 0)
for i in range(linhas):
    for j in range(colunas):
        if matriz1[i][j] > maior_valor:
            maior_valor = matriz1[i][j]
            posicao_maior = (i, j)
        if matriz1[i][j] < menor_valor:
            menor_valor = matriz1[i][j]
            posicao_menor = (i, j)

print(f'O maior valor é: {maior_valor} e a posção é: {posicao_maior}')
print(f'O menor valor é: {menor_valor} e a posição é: {posicao_menor}')

print()

#Procurar por um elemento na Matriz. Se encontrar, retornar a posição do mesmo. Caso exista mais de um elemento igual, mostrar as posições de todos.
escolha = 4
if escolha == 4:
    posicao_valor_encontrada = (0, 0)
    elemento_procurado = int(input('Digite o número que você queira encontrar na matriz: '))
    for i in range(linhas):
        for j in range(colunas):
            if matriz1[i][j] == elemento_procurado:
                posicao_valor_encontrada = (i, j)
                print(f'A posição dele é: {posicao_valor_encontrada}')

print()

#Calcular e exibir a matriz transposta (Trocar linhas por colunas). Para a transposição da matriz, crie uma nova matriz e reorganize os elementos.
matriz_nova = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(matriz1[j][i])
    matriz_nova.append(linha)

print('Matriz transposta: ')
for i in range(linhas):
    for j in range(colunas):
        print(f'{matriz_nova[i][j]:7}', end = '')
    print()

print()

#Multiplicar a matriz por um fator escalar. - Multiplique todos os elementos da matriz por esse escalar e mostrar a matriz depois.   

        
        
        
        

    
        

