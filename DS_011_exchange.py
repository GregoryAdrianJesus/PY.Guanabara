print('\033[4;31m Convert real in dollar')
real = float(input('\033[1;32m Enter value in real: '))
d = real / 4.79
e = real / 5.38
print(f'\033[1;36m The value intered is equivalent to \033[4;33m ${d:.2f} dollars and \033[4;31m {e:.2f} euros')