from random import randint
num_procurado = 30
list_num_aleatorio = []
posicao = []


for i in range (15):
    list_num_aleatorio.append(randint(27, 40))
print(list_num_aleatorio)
    # então o 'i' é a posição do vetor, posição = 0 verifica se o número é igual a 30, caso nao, passa pra prox, posição = 1, se for verdadeiro, adiciona na lista (posicao)
for i, num in enumerate(list_num_aleatorio):
    if num == num_procurado:
        posicao.append(i)
if not posicao:
    print('Não há o número 30 na lista.')
else:
    print(f'As posições do número 30 são: {posicao}')
