print('=' * 15, 'SOMA DE NÚMEROS ÍMPARES', '=' * 15)
soma = 0
for a in range(1, 500, 2):
    print(a)
    if a % 3 == 0:
        soma = soma + a
print(soma)
