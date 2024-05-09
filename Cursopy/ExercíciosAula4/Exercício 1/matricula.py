class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Disciplina:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def matricular_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} matriculado na disciplina {self.nome}")

    def listar_alunos(self):
        print(f"Alunos matriculados na disciplina {self.nome}:")
        for aluno in self.alunos:
            print(aluno.nome)



if __name__ == "__main__":

    aluno1 = Aluno("João", "001")
    aluno2 = Aluno("Maria", "002")
    aluno3 = Aluno("Pedro", "003")

   
    disciplina = Disciplina("Matemática")

    
    disciplina.matricular_aluno(aluno1)
    disciplina.matricular_aluno(aluno2)
    disciplina.matricular_aluno(aluno3)

    
    disciplina.listar_alunos()
