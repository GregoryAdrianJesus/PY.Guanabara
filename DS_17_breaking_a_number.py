from math import trunc
print('\033[4;31m Turning a broken number into a whole number')
qb = float(input('enter a number with decimal places: '))
inteiro = trunc (qb)
print(f'\033[1;33m The number {qb} has its interger part: {inteiro} ')