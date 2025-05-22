primeiro_vetor = []
segundo_vetor = []
resultante1 = []
resultante2 = []
soma_segundo_vetor = 0


from random import randint

for i in range(10):
    primeiro_vetor.append(randint(1,50)) #Primeira lista
for i in range(5):
    segundo_vetor.append(randint(1,20)) #Segunda lista


for i in range(5):
    soma_segundo_vetor += segundo_vetor[i] # Aqui é a soma do segundo vetor para implementar na soma do vetor resultante 1

for i in range(10):
    if primeiro_vetor[i] % 2 == 0: 
        resultante1.append(primeiro_vetor[i] + soma_segundo_vetor)

for i in range(10):
    if primeiro_vetor[i] % 2 == 1:
        qntd = 0
        for j in range(5):
            if primeiro_vetor[i] % segundo_vetor[j] == 0 and segundo_vetor[j] != 0:
                qntd += 1
        resultante2.append(qntd)
            
print(f'Lista dos vetores\n{primeiro_vetor}\n{segundo_vetor}')

print(f'\nPrimeiro vetor resultante {resultante1}')
print(f'Segundo vetor resultante {resultante2}')


input('\nPressione Enter para fechar o programa...')

