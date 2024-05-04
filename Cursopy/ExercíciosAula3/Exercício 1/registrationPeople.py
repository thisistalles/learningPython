class Person:
    def __init__(self, nome=None, idade=None, signo=None, sangue=None, peso=None, cor_olhos=None, altura=None, hobbies=None):
        self.nome = nome
        self.idade = idade
        self.signo = signo
        self.sangue = sangue
        self.peso = peso
        self.corolhos = cor_olhos
        self.altura = altura
        self.hobbies = hobbies


class Clinic:
    def __init__(self, Person):
        self.__person = Person

    def show_information(self):
        print("Nome:", self.__person.nome)
        print("Idade:", self.__person.idade)
        print("Tipo Sanguíneo:", self.__person.sangue)
        print("Peso:", self.__person.peso)
        print("Altura: ", self.__person.altura)


class Esotericism:
    def __init__(self, person):
        self.__person = person

    def show_information(self):
        print("Nome:", self.__person.nome)
        print("Idade:", self.__person.idade)
        print("Signo do zoadíco:", self.__person.signo)


class Socialmidia:
    def __init__(self, person):
        self.__person = person

    def show_information(self):
        print("Nome:", self.__person.nome)
        print("Idade:", self.__person.idade)
        print("Cor dos olhos:", self.__person.corolhos)
        print("Hobbies:", self.__person.hobbies)
        print("Altura:", self.__person.altura)


Alex = Person(nome='Alex', idade=30, sangue='A+', peso=80, altura=1.80)

Maria = Person(nome = 'Maria', idade = 20, signo ='Touro')

Jonas = Person(nome = 'Jonas', idade = 18, cor_olhos ='Castanho', hobbies ='Programar', altura = 1.60)

clinic = Clinic(Alex)
esoterica = Esotericism(Maria)
socialmidia = Socialmidia(Jonas)

print('\n')
clinic.show_information()
print('\n')
esoterica.show_information()
print('\n')
socialmidia.show_information()
print('\n')

#Tive ajuda tiscle