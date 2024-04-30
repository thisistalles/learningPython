quantity = float(input('Digite a quantidade de dólares $ '))
change = float(input('Digite a taxa de câmbio atual: '))
conversion = round(quantity*change, 2)
print('€', conversion)
