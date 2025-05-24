
matriz = []
todos_nomes = []


medias = []


for i in range(3):
    nome = input(f'\nDigite o nome do {i + 1}° aluno: ')
    todos_nomes.append(nome)
    linha = []
    for j in range(5):
        linha.append(float(input(f'Digite a nota da {j + 1}° prova: ')))
    matriz.append(linha)


for i in range(3):
    soma = 0
    for j in range(5):
        soma += matriz[i][j]
    medias.append(soma / 5)


for i in range(3):
    if medias[i] >= 6:
        print(f'{todos_nomes[i]} media: {medias[i]} situação: Aprovado')
    
    if 4 <= medias[i] < 6:
        print(f'{todos_nomes[i]} media: {medias[i]} situação: Exame')
        
    if  medias[i] < 4:
        print(f'{todos_nomes[i]} media: {medias[i]} situação: Reprovado')
print()

for i in range(len(todos_nomes)):
    print(f'{todos_nomes[i]:7}', end= '')
    for j in range(len(matriz[i])):
        print(f'{matriz[i][j]:7}', end= '')
    print()



