print('=' * 10, 'ANO BISSEXTO', '=' * 10)
from datetime import date
ano = int(input('Diga um ano e veremos se ele é bissexto! Digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
