print('=' * 15, 'PESO DE 5', '=' * 15)
maior = 0
menor = 0
for a in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa ? '.format(a)))
    if a == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
