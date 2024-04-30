import math

cateto1 = float(input('Insira o comprimento do primeiro cateto: '))
cateto2 = float(input('Insira o comprimento do segundo cateto: '))

calc = math.hypot(cateto1, cateto2)
hipotenusa = round(calc, 2)

print('O comprimento da hipotenusa é: ', hipotenusa)