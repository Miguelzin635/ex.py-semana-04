matriz = []
todos_nomes = []

medias = []
soma_geral = 0

for i in range(15):
    nome = input(f'\nDigite o nome do {i + 1}° aluno: ')
    todos_nomes.append(nome)
    linha = []
    for j in range(5):
        linha.append(float(input(f'Digite a nota da {j + 1}° prova: ')))
    matriz.append(linha)


for i in range(15): # Cálculo da média de cada um
    soma = 0
    for j in range(5):
        soma += matriz[i][j]
    medias.append(soma / 5)


for i in range(15): # Print da Média de cada um 
    if medias[i] >= 6:
        print(f'{todos_nomes[i]} media: {medias[i]:.2f} situação: Aprovado')
    
    if 4 <= medias[i] < 6:
        print(f'{todos_nomes[i]} media: {medias[i]:.2f} situação: Exame')
        
    if  medias[i] < 4:
        print(f'{todos_nomes[i]} media: {medias[i]:.2f} situação: Reprovado')


for i in range(15): # Média geral
    soma_geral += medias[i]
media_geral = soma_geral / 15

print()
print(f'A média da classe é de: {media_geral:.2f}') #  Média da classe
print()

for i in range(len(todos_nomes)): # Print da matriz arrumada
    print(f'{todos_nomes[i]:7}', end= '')
    for j in range(len(matriz[i])):
        print(f'{matriz[i][j]:7.2f}', end= '')
    print()


print('\nPressione Enter para fechar o programa...')
