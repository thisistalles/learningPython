lista_vogais = ['a', 'e', 'i', 'o', 'u']
quantidade_vogais = 0

word = input('Digite uma palavra: ').lower()

for c in word:
    if c in lista_vogais:
        quantidade_vogais += 1

print(f'A palavra {word} tem {quantidade_vogais} vogais.')