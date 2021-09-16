print('=' * 15, 'FORMANDO UM TRIÂNGULO v2.0', '=' * 15)
# primeiro exercício
r1 = float(input('Digite uma reta: '))
r2 = float(input('Digite outra reta: '))
r3 = float(input('Digite mais uma reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
# Tipos de Triângulos de acordo com os lados.
if r1 == r2 == r3:
    print('As retas formam um Equilátero.')
elif r1 == r2 or r1 == r3:
    print('As retas formam um Isósceles.')
else:
    print('As retas formam um Escaleno.')
