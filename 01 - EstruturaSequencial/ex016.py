size = float(input('What is the size of the wall in square meters? '))

value = 0
amount_of_cans = 0
liters = 0

if size % 3 != 0:
    liters = 1

liters += size // 3 

if liters % 18 != 0:
    value = 80
    amount_of_cans = 1

amount_of_cans += liters // 18
value += amount_of_cans * 80

print('Total liters needed: ', liters)
print('Value total: R$', value)
