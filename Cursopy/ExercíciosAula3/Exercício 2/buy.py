buy = float(input('Digite o valor da compra: '))
if buy >= 100 and buy < 200:
    desc = (buy*10)/100
    valdesc = buy - desc
    print('Você recebeu 10% de desconto:', valdesc)
elif buy >= 200:
    desc = (buy*20) / 100
    valdesc = buy - desc
    print('Você recebeu 20% de desconto:', valdesc)
