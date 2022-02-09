print('=' * 15, 'PAGAMENTO DE UM PRODUTO', '=' * 15)
preco = float(input('Digite o preço do produto: R$'))
print('=' * 5, 'Forma de Pagamento', '=' * 5)
print("""Digite 1 para Dinheiro a vista ou Cheque.
Digite 2 para Cartão a vista.
Digite 3 para Cartão em 2x
Digite 4 para cartão com 3x ou mais""")
escolha = int(input(''))
# Dinheiro a vista ou cheque.
vista = (10 * preco) / 100
vista2 = preco - vista
# Cartão a vista
vistac = (5 * preco) / 100
vistac2 = preco - vistac
# A pagar
if escolha == 1:
    print('O produto de R${:.2f} ficará a vista com 10% de desconto e sairá por R${:.2f}'.format(preco, vista2))
elif escolha == 2:
    print('O produto de R${:.2f} ficará a vista no cartão tem 5% de desconto e sairá por R${:.2f}'.format(preco, vistac2))
elif escolha == 3:
    print('O produto em 2x no cartão fica pelo preço normal de R${:.2f}'.format(preco))
elif escolha == 4:
    dividir = int(input('O quanto quer divirdir ? '))
    # Juros de 20%
    juros = preco * 0.2 * dividir
    print('O valor do produto R${:.2f} com juros de 20% em {}x fica por R${:.2f}'.format(preco, dividir, juros))
