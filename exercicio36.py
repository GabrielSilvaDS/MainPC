print('=' * 15, 'CALCULANDO AUMENTO', '=' * 15)
salario = float(input('Digite seu salário: R$'))
aumento = salario + (salario * 15 / 100)
aumento2 = salario + (salario * 10 / 100)
if salario >= 1.250:
    print('Você recebeu um aumento de 10%! Seu salário é de R${:.2f}'.format(aumento2))
else:
    print('Você recebeu um aumento de 15%! Seu salário é de R${:.2f}'.format(aumento))
