print('=' * 15, 'MAIORES', '=' * 15)
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for a in range(1 , 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu ? '.format(a)))
    idade = atual - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E {} pessoas menores de idade'.format(menor))
