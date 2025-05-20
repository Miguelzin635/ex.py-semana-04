total_vendas = []
total_nomes = []
total_comissao = []


for j in range(3):
    nomes = input('Digite o nome do vendedor: ')
    total_nomes.append(nomes)

for i in range(3):
    vendas = float(input(f'Do vendedor {nomes[i]} informe o total das vendas: '))
    total_vendas.append(vendas)

for i in range(3):
    comissao = float(input(f'Do vendedor {nomes[i]} informe o percentual de comissão(%): '))
    total_comissao.append(comissao)







vendas = []
nomes = []
total_comissao = []

for i in range(3):
    total_nomes = input('\nDigite o nome do vendedor: ')
    nomes.append(total_nomes)
    total_vendas = float(input(f'{nomes[i]} informe o total das vendas: '))
    vendas.append(total_vendas)
    comissao = float(input(f'Do vendedor {nomes[i]} informe o percentual de comissão(%): '))
    total_comissao.append(comissao)


print(vendas)
print(nomes)
    
