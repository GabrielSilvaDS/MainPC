print('=' * 15, 'NADADORES', '=' * 15)
import datetime
print('Vamos descobrir o grau de nadador que você é com base na sua idade.')
nome = str(input('Digite seu nome: '))
idade = int(input('Ano em que nasceu: '))
# Calculos
data = datetime.date.today().year
nasc = data - idade
# Resultados
if nasc <= 9:
    print('{} você tem {} anos e seria um nadador Mirim!'.format(nome, nasc))
elif nasc <= 14:
    print('{} você tem {} anos e seria um nadador Infantil!'.format(nome, nasc))
elif nasc <= 19:
    print('{} você tem {} anos e seria um nadador Junior!'.format(nome, nasc))
elif nasc <= 20:
    print('{} você tem {} anos e seria um nadador Sênior!'.format(nome, nasc))
elif nasc > 20:
    print('{} você tem {} anos e seria um nadador Master!!'.format(nome, nasc))
