print('=' * 15, 'PEDRA, PAPEL E TESOURA', '=' * 15)
from random import randint
lista = ('pedra', 'papel', 'tesoura')
comp = randint(0, 2)
print('[0] Pedra\n[1] Papel\n[2] Tesoura')
jogador = int(input('Escolha: '))
if comp == 0:  # PEDRA
    if jogador == 0:
        print('Você escolheu {} e eu escolhi {} empatamos!!'.format(lista[jogador], lista[comp]))
    elif jogador == 1:
        print('Você escolheu {} e eu escolhi {} você venceu!!'.format(lista[jogador], lista[comp]))
    elif jogador == 2:
        print('Você escolheu {} e eu escolhi {} você perdeu!!'.format(lista[jogador], lista[comp]))
    else:
        print('JOGADA INVÁLIDA')

elif comp == 1:  # PAPEL

    if jogador == 0:
        print('Você escolheu {} e eu escolhi {} você perdeu!!'.format(lista[jogador], lista[comp]))
    elif jogador == 1:
        print('Você escolheu {} e eu escolhi {} empatamos!!'.format(lista[jogador], lista[comp]))
    elif jogador == 2:
        print('Você escolheu {} e eu escolhi {} você venceu!!'.format(lista[jogador], lista[comp]))
    else:
        print('JOGADA INVÁLIDA')
elif comp == 2:  # TESOURA
    if jogador == 0:
        print('Você escolheu {} e eu escolhi {} você venceu!!'.format(lista[jogador], lista[comp]))
    elif jogador == 1:
        print('Você escolheu {} e eu escolhi {} você perdeu!!'.format(lista[jogador], lista[comp]))
    elif jogador == 2:
        print('Você escolheu {} e eu escolhi {} empatamos!!'.format(lista[jogador], lista[comp]))
    else:
        print('JOGADA INVÁLIDA')
