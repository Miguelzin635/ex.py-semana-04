todos_nomes = []
todas_medias = []
maior_media = 0

exames = []
nome_exam = []


for i in range(3):
    nome = input(f'\nDigite o nome do {i + 1}° aluno: ')
    todos_nomes.append(nome)
    media = float(input('Informe a média final desse aluno: '))
    todas_medias.append(media)


for i in range(3):
    if todas_medias[i] > maior_media:
        maior_media = todas_medias[i]
        nome_maior = i

    if todas_medias[i] < 7:
        exame_aprov = 10 - todas_medias[i]
        exames.append(exame_aprov) # Vai guardar o quanto falta de cada um para ser aprovado
        nome_exam.append(todos_nomes[i]) # Vai guardar todos os nomes com média menor que 7
        

print(f'\nO aluno {todos_nomes[nome_maior]} é o que tem a maior média, que é: {maior_media:.2f}')

print('\nJá para os alunos que ficaram com média menor que 7.00: ')
for i in range(len(nome_exam)): # O len é o tamanho da lista, entao se tiver 2 de exame vai ser range(2) no caso os indices 0, 1 (que seriam os primeiros elementos)
    print(f'O aluno {nome_exam[i]} precisa tirar {exames[i]:.2f} no exame para ser aprovado.')


input('\nPressione Enter para fechar o programa...')

