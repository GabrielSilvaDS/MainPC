print('=' * 15, 'ANALISADOR', '=' * 15)
soma = 0
media = 0
maioridadem = 0
nomevelho = ''
mulhermenor = 0
for a in range(1, 5):
    print('\033[0;33m-=-\033[m' * 6, '{}ª PESSOA'.format(a), '\033[0;33m-=-\033[m' * 6)
    nome = str(input('nome: '))
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).upper()
    soma += idade
    if sexo == 'M' and idade > maioridadem:
        maioridadem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
media = soma / 4
print('Média de idade é {:.0f}'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nomevelho, maioridadem))
print('Ao todo são {} mulher(es) com menos de 20 anos'.format(mulhermenor))
