from math import pow,sqrt
print('\033[4;34m Find the hypotenuse of a right triangle')
cateto1 = float(input('Enter length of first side: '))
cateto2 = float(input('Enter length of second side: '))
elevado = pow(cateto1,2) + pow(cateto2,2)
raiz = sqrt(elevado)
print(f'\033[4;35m The right trangle with of length of {cateto1}cm and {cateto2}cm has a hypotenuse of {raiz}cm')
