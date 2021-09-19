print('=' * 15, 'TABUADA', '=' * 15)
numero = int(input('Digite um número: '))
for a in range(1, 11):
    multi = numero * a
    print('{} * {} = {}'.format(numero, a, multi))
