age = int(input('Digite a idade: '))

if age >= 0 and age <= 12:
    print('Idade', age, '= Criança')
elif age >= 13 and age <= 17:
    print('Idade: ', age, '= Adolescente')
elif age >= 18 and age <= 64:
    print('Idade: ', age, '= Adulto')
elif age >= 65:
    print('Idade: ', age, '= Idoso')
