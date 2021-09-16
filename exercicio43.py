print('=' * 15, 'BOLETIM', '=' * 15)
nome = str(input('Digite seu nome: '))
nm1 = float(input('Nota da terceira unidade de Matemática: '))
np1 = float(input('Nota da terceira unidade de Português: '))
nm2 = float(input('Nota da quarta unidade de Matemática: '))
np2 = float(input('Nota da quarta unidade de Português: '))
# média 7
medianm = float((nm1 + nm2) / 2)
medianp = float((np1 + np2) / 2)
# Nota de Matemática
if medianm >= 7:
    print('SUA MÉDIA FOI DE {:.1f} VOCÊ ESTÁ APROVADO!!!'.format(medianm))
elif medianm < 5:
    print('SUA MÉDIA FOI DE {:.1f} VOCÊ ESTÁ REPROVADO!!! ESTUDE MAIS.'.format(medianm))
elif medianm >= 5 or medianm <= 6.9:
    print('SUA MÉDIA FOI DE {:.1f} VOCÊ ESTÁ DE RECUPERAÇÃO!!! ESTUDE E BOA SORTE.'.format(medianm))
# Nota de Português
if medianp >= 7:
    print('SUA MÉDIA FOI DE {:.1f} VOCÊ ESTÁ APROVADO!!!'.format(medianp))
elif medianp < 5:
    print('SUA MÉDIA FOI DE {:.1f} VOCÊ ESTÁ REPROVADO!!! ESTUDE MAIS.'.format(medianp))
elif medianp >= 5 or medianp <= 6.9:
    print('SUA MÉDIA FOI DE {:.1f} VOCÊ ESTÁ DE RECUPERAÇÃO!!! ESTUDE E BOA SORTE.'.format(medianp))
