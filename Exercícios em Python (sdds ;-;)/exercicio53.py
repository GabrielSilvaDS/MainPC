print('=' * 15, 'SOMA DE NÚMEROS PARES', '=' * 15)
soma = 0
for a in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma = soma + num
print(soma)
