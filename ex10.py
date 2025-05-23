vetor1 = []
vetor2 = []

for i in range(10):
    valor = float(input(f'Digite o {i + 1}° valor: '))
    vetor1.append(valor)

    if vetor1[i] > 0:
        vetor2.append(vetor1[i])

print(f'\nVetro resultante: \n{vetor2}')

input('\nPressione Enter para fechar o programa...')
