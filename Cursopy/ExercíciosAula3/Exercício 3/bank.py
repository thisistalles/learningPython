class Person:
    def __init__(self, nome, identificacao, nacionaliddade):
        self.nome = nome
        self.identificacao = identificacao
        self.nacionalidade = nacionaliddade


class Bank_account:
    def __init__(self, titular, saldo, tipo_conta, tipo_moeda):
        self.titular = titular
        self.saldo = saldo
        self.tipo_conta = tipo_conta
        self.tipo_moeda = tipo_moeda


titular_conta = Person('Roberto Silva', '78945612330', 'Brasileiro')
conta = Bank_account(titular_conta, 1000.00, 'Corrente', 'Real')

print("Titular da conta:", conta.titular.nome)
print("Saldo da conta:", conta.saldo)
print("Tipo de conta:", conta.tipo_conta)
print("Tipo de moeda:", conta.tipo_moeda)
