from math import pow,sqrt
print('Find the hypotenuse of a right triangle')
cateto1 = float(input('Enter length of leg 1°: '))
cateto2 = float(input('Enter length of leg 2°: '))
elevado = pow(cateto1,2) + pow(cateto2,2)
raiz = sqrt(elevado)
print(f'The right trangle with legs of length {cateto1}cm and {cateto1}cm has a hypotenuse of {raiz}cm')
