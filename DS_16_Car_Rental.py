print('Find out how much you will pay for a renting a car')
dia = float(input('How many days using the car?'))
km = float(input('How many Km you will use?'))
pd = dia * 60
pk = km * 0.15
total = pd + pk
print(f'you will pay for days used ${pd} and for km used ${pk} totalizing:${total}')