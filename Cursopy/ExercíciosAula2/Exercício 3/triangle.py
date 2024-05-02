side1 = float(input('Digite a medida do 1º lado do triângulo: '))
side2 = float(input('Digite a medida do 2º lado do triângulo: '))
side3 = float(input('Digite a medida do 3º lado do triângulo: '))

if side1 == side2 and side2 == side3 and side1 == side3:
 print('É um triângulo equilatero. ')
elif side1 != side2 and side2 != side3 and side1 != side3:
 print('É um triângulo escaleno. ')
else:
 print('É um triângulo isósceles. ')