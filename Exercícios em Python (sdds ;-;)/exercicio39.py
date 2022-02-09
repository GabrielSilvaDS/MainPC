print('=' * 15, 'EMPRÉSTIMO PARA CASA NOVA', '=' * 15)
valor = float(input('Qual o valor da casa ? R$'))
salario = float(input('Quanto é o seu salário ? R$'))
anos = int(input('Até quantos anos você deseja pagar a casa ? '))
prestacao = valor / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar a casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(valor, anos, prestacao))
if prestacao <= minimo:
    print('EMPRÉSTIMO ACEITO!')
else:
    print('EMPRÉSTIMO NEGADO!')
