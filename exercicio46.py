print('=' * 15, 'CALCULANDO O IMC', '=' * 15)
nome = str(input('Digite seu nome: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (altura * altura)
if imc < 18:
    print('{} você esta abaixo do peso com {:.1f}.'.format(nome, imc))
elif imc >= 18.5 and imc < 25:
    print('{} você esta no peso ideal com {:.1f}'.format(nome, imc))
elif imc >= 25 and imc < 30:
    print('{} você esta com sobre peso com {:.1f}'.format(nome, imc))
elif imc >= 30 and imc < 40:
    print('{} você esta com obesidade com {:.1f}'.format(nome, imc))
elif imc >= 40:
    print('{} você esta com obesidade mórbida com {:.1f}'.format(nome, imc))
