print('\033[0;32m Pay for the product in cash with a discount or in installments with an incrase?')
produto = float(input('\033[4;35m Enter  the amount in cash payment to 8 percent discount; $'))
dinheiro = produto * 8 / 100
print(f'You get ${dinheiro} off: ')
parcela = float(input('\033[4;35m enter the value of the installments and see the value of the 15 percent incrase: $'))
acrescimo = produto / 100 * 15
print(f'You will pay \033[4;31m ${acrescimo} more than the original amount')
