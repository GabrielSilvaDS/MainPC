print('=' * 15, 'PALÍNDROMOS', '=' * 15)
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
juntar = ''.join(palavra)
inverter = ''
for a in range(len(juntar) -1, -1, -1):
    inverter += juntar[a]
print('O inverso de {} é {}'.format(frase, inverter))
if inverter == juntar:
    print('A frase é um Palíndromo')
else:
    print('A frase não é um palíndromo')

