import datetime

data_nascimento = input("Digite a sua data de nascimento(no formato yyyy-mm-dd): ")
datanascimento = datetime.datetime.strptime(data_nascimento, "%Y-%m-%d").date()

idade = datetime.date.today().year - datanascimento.year

print("Sua idade é: ", idade)
