print('\033[1;35m enter your salary amount and find out how much you earn with 15% increase ')
salario = float(input('enter your salary: '))
aumento = salario * 15 / 100
print(f'You would earn \033[4;34mR${aumento} more')
print(f'Totalizing: \033[4;32mR${salario + aumento}')
