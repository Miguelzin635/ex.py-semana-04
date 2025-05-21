lgc_comp = []
lgc_program = []
iguais = []

print('\nCurso de Lógica Computacional')
for i in range(6):
    matricula_comput = int(input('Digite o número de matrícula do aluno: '))
    lgc_comp.append(matricula_comput)


print('\nCurso de Lógica de Programação')
for i in range(3):
    matricula_program = int(input('Digite o número de matrícula do aluno:  '))
    lgc_program.append(matricula_program)


for i in range(6):
    for j in range(3):
        if lgc_comp[i] == lgc_program[j] and lgc_comp[i] not in iguais:
            iguais.append(lgc_comp[i])
print(f'\nAs listas das matrículas:\n{lgc_comp}\n{lgc_program}')            
print(f'\nMatrículas que estão nos dois cursos: {iguais}')


input('Pressione Enter para fechar o programa...')
