x = input('Digite qualquer coisa: ')

print('O tipo desse valor é ', type(x))
print('Só tem espaços? {}'.format(x.isspace()))
print('É numérico? {}'.format(x.isnumeric()))
print('É alfabetico? {}'.format(x.isalpha()))
print('Está em maiusculas? {}'.format(x.isupper()))
print('Está em minusculas? {}'.format(x.islower()))
print('Está capitalizada? {}'.format(x.istitle()))