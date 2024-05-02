import random

random_number = random.randint(1, 100)

while True:
    user_number = int(input('Digite um número de 1 a 100: '))

    if random_number > user_number:
        print('É maior')
    elif random_number < user_number:
        print('É menor')
    else:
        print('Parabéns você acertou!! ')
        break

