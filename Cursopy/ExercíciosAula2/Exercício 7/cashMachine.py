print('--Caixa Eletrônico--')
cash = 3000

opcoes = 0

while opcoes != 4:

    print('---Options---: ')
    
    print('1. check balance')
    print('2. withdraw')
    print('3. deposit')
    print('4. close')

    opcoes = input('Selecione uma opção: ')

    if opcoes == '4':
        print('Adeus')
        break

##Em fase de acabamento