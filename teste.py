print('=' * 15, 'QUEM É QUEM', '=' * 15)
nomevelhohom = ''
nomenovohom = ''
nomevelhomul = ''
nomenovamul = ''
idadevelhohom = 0
idadenovohom = 0
idadevelhomul = 0
idadenovamul = 0
flagM = 0
flagF = 0
for pess in range(1, 5):
    print('-=-' * 6, '{}ª PESSOA'.format(pess), '-=-' * 6)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Qual seu sexo ? [M/F]: ')).upper()
    if sexo == 'M' and idade > idadevelhohom:
        print('------1')
        idadevelhohom = idade
        nomevelhohom = nome
        if flagM == 0:
            nomenovohom = nome
            idadenovohom = idade
            flagM = 1
    if sexo == 'M' and idade < idadenovohom:
        print('------2')
        nomenovohom = nome
        idadenovohom = idade
    if sexo == 'F' and idade > idadevelhomul:
        print('------3')
        nomevelhomul = nome
        idadevelhomul = idade
        if flagF == 0:
              = nome
            idadenovamul = idade
            flagF = 1
    if sexo == 'F' and idade < idadenovamul:
        print('------4')
        nomenovamul = nome
        idadenovamul = idade
print('O homem mais velho se chama {} e tem {} anos.'.format(nomevelhohom, idadevelhohom))
print('-=-' * 30)
print('A mulher mais velha se chama {} e tem {} anos.'.format(nomevelhomul, idadevelhomul))
print('-=-' * 30)
print('O homem mais novo se chama {} e tem {} anos.'.format(nomenovohom, idadenovohom))
print('-=-' * 30)
print('A mulher mais nova se chama {} e tem {} anos.'.format(nomenovamul, idadenovamul))
print('-=-' * 30)
