print('\033[4;35m know how many liters of paint it will take to paint your wall')
altura = float(input('\033[1;34m enter the height: '))
largura = float (input('\033[3;33m enter the width: '))
area = largura * altura
tinta = area / 2
print(f'\033[04;34m Your wall has \033[33m {altura} X\033[35m {largura} with \033[36m {area:.2f}m² area')
print(f'You need \033[4;33m{tinta:.2f} liters of paint to paint your wall')