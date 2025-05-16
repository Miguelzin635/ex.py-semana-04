from random import randint

vet_numa_aleatorio = []
mult_2 = []
mult_3 = []
mult_2_3 = []
for i in range(7):
    vet_numa_aleatorio.append(randint(1, 50))    
    if vet_numa_aleatorio[i] % 2 == 0:
        mult_2.append(vet_numa_aleatorio[i])
    
    if vet_numa_aleatorio[i] % 3 == 0:
        mult_3.append(vet_numa_aleatorio[i])


    if vet_numa_aleatorio[i] % 2 == 0 and vet_numa_aleatorio[i] % 3 == 0:
        mult_2_3.append(vet_numa_aleatorio[i])

if not mult_2_3:
    print('lista vazia')
else:
    print(mult_2_3)
    
print(mult_2)
print(mult_3)

input('Pressione Enter para fechar o programa...')
