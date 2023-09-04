from math import sin,cos,tan
print('\033[4;33m Find the sine, cosine and tangent of any angle')
angulo = float(input('\033[1;32m enter an angle: '))
seno = sin(angulo)
print(f'\033[1;32m The sine of the angle is: {seno}')
cosseno = cos(angulo)
print(f'\033[2;34m the cosine of the angle is: {cosseno}')
tangente = tan(angulo)
print(f'\033[2;35m The tangent of the angle is: {tangente}')

