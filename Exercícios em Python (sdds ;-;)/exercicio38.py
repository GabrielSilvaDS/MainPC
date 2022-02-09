print('=' * 15, 'COLOCANDO CORES', '=' * 15)
nome = str(input('Digite seu nome: '))
print('Olá {}{}{}! É um prazer te conhecer.'.format('\033[4;35m', nome, '\033[m'))
