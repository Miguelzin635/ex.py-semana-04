todas_vendas = []
todos_nomes = []
todas_comissao = []
total_vendas = 0
soma = 0
comissao_calculada = []
maior_valor = 0

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
    print('-'*46)
    total_receber = (todas_vendas[i] * todas_comissao[i] / 100)
    print(f'Do vendedor {todos_nomes[i]} o valor a receber é: {total_receber:.2f} ')
print('-'*46)

for i in range(3):
    total_vendas += todas_vendas[i]
print(f'A soma total de vendas é: R${total_vendas:.2f}')


for i in range(3):
    # comissao_calculada são todas as comissões calculadas, ja o maior_valor é a maior comissão
    valor_comissao = (todas_vendas[i] * todas_comissao[i] / 100)
    comissao_calculada.append(valor_comissao)

    # Aqui compara com o primeiro indice(o 0 no caso) assumindo o valor, entao o maior_valor vai ser o primeiro valor_copmissao, assim como o menor_valor
    if i == 0:
        maior_valor = valor_comissao
        menor_valor = valor_comissao
        nome_maior = i
        nome_menor = i

    elif valor_comissao > maior_valor:
        maior_valor = valor_comissao
        # O nome_maior vai guardar dentro desse for o índice (nome do vendedor) cujo qual tem maior comissão(maior_valor)
        nome_maior = i
    elif valor_comissao < menor_valor:
        menor_valor = valor_comissao
        nome_menor = i
        
print(f'\nO maior valor a receber é R${maior_valor:.2f} do vendedor {todos_nomes[nome_maior]}')
print(f'\nO menor valor a receber é R${menor_valor:.2f} do vendedor {todos_nomes[nome_menor]}')


input('Pressione Enter para fechar o programa...')
