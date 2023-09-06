from random import shuffle
print('\033[2;35m select order of items')
item1 = input('\033[1;34m enter the item:')
item2 = input('\033[1;31m enter the second item:')
item3 = input('\033[1;33m enter the third item:')
lista = [item1,item2,item3]
shuffle(lista)
print(f'The order of the changed items is:{lista}')
