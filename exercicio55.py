print('=' * 15, 'NÚMEROS PRIMOS', '=' * 15)
while True:
    num = int(input('Digite um número: '))
    if num == 00:
        break
    if num == 2 or num == 3 or num == 5:
        print('O número {} é um número primo'.format(num))
    elif num == 1:
        print('O número {} não é um número primo'.format(num))
    elif num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        print('O número {} não é um número primo'.format(num))
    else:
        print('O número {} é um número primo'.format(num))
