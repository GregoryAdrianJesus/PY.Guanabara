import random
print('\033[4;33m jewelry raffle')
joia1 = str(input('\033[1;32m insert the first jewel:'))
joia2 = str(input('\033[1;34m Insert the second jewel:'))
joia3 = str(input('\033[1;35m insert the third jewel:'))
lista = [joia1,joia2,joia3]
print('\033[2;36m The selected jewels was:',(random.choice(lista)))
