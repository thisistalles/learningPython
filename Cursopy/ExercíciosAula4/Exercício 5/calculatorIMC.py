weight = float(input('Digite o seu peso(em quilogramas) '))
height = float(input('Digite o sua altura(em metros) '))
imc = round(weight/(height**2), 2)
print('Seu IMC é: ', imc)