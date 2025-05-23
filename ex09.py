produto = []
codigo = []
preco = []
novo_preco_codigo = []
novo_preco_1000 = []
novo_preco_cd1000 = []

nova_lista_cd1000 = []

for i in range(3):
    produto.append(input(f'Informe o nome do {i +1}° produto: '))
for i in range(3):
    codigo.append(input(f'Informe o código do {i + 1}° produto: '))
for i in range(3):
    preco.append(float(input(f'Informe o preço do {i + 1}° produto: R$')))

print(f'Relatório: ')
print('-'*70)
for i in range(3):
    if (codigo[i] == 'par' or codigo[i] == 'PAR' or codigo[i] == 'Par') and preco[i] > 1000:
        novo_preco_cd1000.append(preco[i] + (preco[i] * 0.20))

    elif codigo[i] == 'par' or codigo[i] == 'PAR' or codigo[i] == 'Par':
        novo_preco_codigo.append(preco[i] + (preco[i] * 0.15))       

    elif preco[i] > 1000:
        novo_preco_1000.append(preco[i] + (preco[i] * 0.10))    
       
else: 
        
        
    print(f'{i + 1}° produto: {produto[i]}\t\t{codigo[i]}\t\t{preco[i]}\t\t{nova_lista_cd1000}')


    
