matriz = []

meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril']

soma_ano = 0

for i in range(4):
    print(f'No mês de {meses_ano[i]}')
    linha = []
    for j in range(4):
        linha.append(float(input(f'Digite o valor de venda da {j + 1}° semana: R$'))) # Linha são os valores de vendas de toda a matriz
    matriz.append(linha)


####
print(f'\nRelatório de vendas anual: \n', '-'*80)
print(f'{'Semanas:':<16}{'1° semana':<17} {'2° semana':<17} {'3° semana':<17} {'4° semana':<20}')

for i in range(4):      #Print da matriz arrumada de todos os meses seguido de total de vendas da semana
    print(f'{meses_ano[i]:16}', end= '')
    for j in range(4):
        print(f'R${matriz[i][j]:<16.2f}', end= '')
    print()

print('-'*80)
####
print()

for i in range(4):   # Total vendido em cada mes do ano
    soma_mes = 0
    for j in range(4):
        soma_mes += matriz[i][j]
    print(f'O total vendido no mês de {meses_ano[i]} é: R${soma_mes:.2f}')


for i in range(4):
    for j in range(4):
        soma_ano += matriz[i][j]
print(f'\nO total vendido pela loja no ano todo é: R${soma_ano:.2f}')

input('\nPressione Enter para fechar o programa...')
    
