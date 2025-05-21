todas_vendas = []
todos_nomes = []
todas_comissao = []
total_vendas = 0
soma = 0
total = []
auxiliar = 0

for i in range(3):
    nomes = input('Digite o nome do vendedor: ')
    todos_nomes.append(nomes)

for i in range(3):
    vendas = float(input(f'Do vendedor {todos_nomes[i]} informe o total das vendas: '))
    todas_vendas.append(vendas)

for i in range(3):
    comissao = float(input(f'Do vendedor {todos_nomes[i]} informe o percentual de comissão(%): '))
    todas_comissao.append(comissao)


print('\nRelatório: ')
for i in range(3):
    print('-'*40)
    total.append(todas_vendas[i] * todas_comissao[i] / 100)
    print(f'{todos_nomes[i]}: valor {total:.2f} ')
print('-'*40)

for i in range(3):
    total_vendas += todas_vendas[i]
print(f'A soma total de vendas é: {total_vendas}')


for i in range(3):
    if total[i] > auxiliar:
        auxiliar = total[i]

        



print(todos_nomes)
print(todas_vendas)
print(todas_comissao)
