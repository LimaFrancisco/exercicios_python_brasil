excess = 0
assessment = 0
weight = float(input('Enter the weight: '))

if weight > 50:
    excess = weight - 50
    assessment = excess * 4

print('*' * 10, 'PROGRAM`S DATA', '*' * 10)
print('fixe`s weight: ', weight, 'kg')
print('excess: ', excess, 'kg')
print('assessment: R$', assessment)
