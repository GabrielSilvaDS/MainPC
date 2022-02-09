print('=' * 15, 'CONVERSOR BINÁRIO', '=' * 15)
numero = int(input('Digite um número: '))
print('[1] Digite para Binário\n[2] Digite para Octal\n[3] Digite para Hexadecimal')
escolha = int(input('Escolha: '))
if escolha == 1:
    print('{} em Binário fica {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} em Octal fica {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} em Hexadecimal fica {}'.format(numero, hex(numero)[2:]))
else:
    print('tu é doido ? tem 3 opções e tu escolhe a que não tem ?? faz de novo!')
