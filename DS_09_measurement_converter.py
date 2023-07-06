print('\033[1;32m Enter a distance in meters and find your conversion')
m = float(input('Distance in meters:'))
km = m / 1000
print (f'\033[4;34m Kilometers: {km}km')
dam = m / 10 
print(f'\033[4;33m Decameters: {dam}dam')
hm = m / 100
print(f'\033[4;35m hectometers: {hm}hm')
dm = m * 10
print(f'\033[4;33m Decimeters: {dm}dm')
cm = m * 100
print(f'\033[4;35m Centimeters: {cm}cm')
mm = m * 1000
print(f'\033[4;34m Milimeters: {mm}mm')

      
      


