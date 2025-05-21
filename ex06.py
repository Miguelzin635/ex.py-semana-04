todos_valores = []
qntd_negativos = 0
soma = 0

for i in range(10):
    valores = float(input(f'Digite o {i + 1}° valor: '))
    todos_valores.append(valores)
    if todos_valores[i] < 0:
        qntd_negativos += 1
for i in range(10):
    if todos_valores[i] > 0:
        soma += todos_valores[i]

print(f'\nA soma de todos os valores positivos: {soma:.2f}')
print(f'A quantidade de valores negativos: {qntd_negativos}')

input('Pressione Enter para fechar o programa...')
