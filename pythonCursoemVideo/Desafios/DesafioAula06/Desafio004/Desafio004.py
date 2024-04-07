d = input('Digite algo: ')
print('Foi digitado "{}" '.format(d))
print('O tipo primitivo desse valor é', type(d))
print(' "{}" É um número?'.format(d), d.isnumeric())
print(' "{}" É uma letra?'.format(d), d.isalpha())
#Olhando a resolução do exercício completo ele fez com mais coisas mas essa é minha versão