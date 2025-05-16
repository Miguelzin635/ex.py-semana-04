import random
vet_num_aleatrio = []
mostra_par = []
qntd_par = 0
mostra_impar = []
qntd_impar = 0
for i in range (6):
    vet_num_aleatrio.append(random.randint(1, 100))
    if vet_num_aleatrio[i] % 2 == 0:
        mostra_par.append(vet_num_aleatrio[i])
        qntd_par += 1
    else:
        mostra_impar.append(vet_num_aleatrio[i])
        qntd_impar += 1
print(f'Os númeors pares: {mostra_par}\nQuantidade de pares: {qntd_par}')
print(f'Os números ímpares: {mostra_impar}\nQuantidade de ímpares: {qntd_impar}')

input('\nPressione Enter para fechar o programa...')
