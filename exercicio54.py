print('=' * 15, 'PROGRESSÃO ARITMÉTICA', '=' * 15)
pt = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
for a in range(1, 11):
    resp = pt + (a - 1) * r
    print(resp)
    