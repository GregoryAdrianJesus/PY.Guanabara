print('\033[4;34m <<<Enter a number and find your multiplication table>>>')
tb = float(input('\033[1;31m enter a number:'))
print('\033[32m ~' * 15)
for i in range(1,11):
    r = i * tb
    print(f'{tb} X {i} = {r}')
print('\033[32m ~' * 15)


