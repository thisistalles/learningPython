print('--SIEP--')
aluno = str(input('Digite o nome do Aluno: '))

faltas = str(input('O Aluno faltou em alguma das provas?(s/n): ').lower())
if faltas == 's':
    ambas = input('Em ambas?(s/n): ').lower()
    if ambas == 's':
        print(f'Aluno {aluno} Reprovado')
    else:
        materia = str(input('Digite a matéria que ele faltou: '))
        print(f'Aluno {aluno} faça a prova de {materia}')
else:
    progamacao = float(input('Digite a nota em progamação: '))
    matematica = float(input('Digite a nota em Matemática: '))

    if progamacao >= 60.0 and matematica >= 60.0:
        print(f'Aluno{aluno} aprovado!')
    else:
        print(f'Aluno {aluno} reprovado.')
