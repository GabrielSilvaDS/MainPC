print('=' * 15, 'ALISTAMENTO MILITAR', '=' * 15)
import datetime
nome = str(input('Digite seu nome: '))
nasc = int(input('Informe o ano de nascimento: '))
data = datetime.date.today().year
idade = data - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, data))
if idade == 18:
    print('NECESSÁRIO ALISTAMENTO MILITAR!!')
elif idade < 18:
    falta = 18 - idade
    print('AINDA FALTA(M) {} ANO(S) PARA O ALISTAMENTO'.format(falta))
else:
    falta = idade - 18
    print('JÁ DEVERIA TER SE ALISTADO HÁ {} ANO(S)'.format(falta))
