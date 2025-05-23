produto = []
codigo = []
preco = []

for i in range(3):
    produto.append(input(f'Informe o nome do {i +1}° produto: '))
for i in range(3):
    codigo.append(int(input(f'Informe o código do {i + 1}° produto: ')))
for i in range(3):
    preco.append(float(input(f'Informe o preço do {i + 1}° produto: R$')))

print(f'Relatório:\n{'Produto':<20} {'Código':<15} {'Preço':<20}{'novo_preco':<15} ')
print('-'*65)
for i in range(3):
    codigo_par = codigo[i] % 2 == 0
    preco_maior_1000 = preco[i] > 1000
    
    if codigo_par and preco_maior_1000:
        novo_preco = preco[i] + (preco[i] * 0.20)
        print(f'{produto[i]:<20} {codigo[i]:<15} {preco[i]:<19.2f} {novo_preco:<19.2f}')
    elif codigo_par:
        novo_preco = preco[i] + (preco[i] * 0.15)
        print(f'{produto[i]:<20} {codigo[i]:<15} {preco[i]:<19.2f} {novo_preco:<19.2f}')
    elif preco_maior_1000:
        novo_preco = preco[i] + (preco[i] * 0.10)
        print(f'{produto[i]:<20} {codigo[i]:<15} {preco[i]:<19.2f} {novo_preco:<19.2f}')
    else: 
        print(f'{produto[i]:<20} {codigo[i]:<15} {preco[i]:<19.2f} {'Sem aumento!':<15}')
print('-'*65)


input('Pressino Enter para fechar o programa...')
