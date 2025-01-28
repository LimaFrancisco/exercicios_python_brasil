value_per_hour = float(input('Enter the value per hour: '))
hour_value = float(input('Enter the value of the hour: '))

gross_salary = value_per_hour * hour_value
IR = gross_salary * 0.11
INSS = gross_salary * 0.08
sindicate = gross_salary * 0.05
net_salary = gross_salary - (IR + INSS + sindicate)

print('+ Salario Bruto : R$', gross_salary)
print('- IR (11%) : R$', IR)
print('- INSS (8%) : R$', INSS)
print('- Sindicato (5%) : R$', sindicate)
print('= Salario Liquido : R$', net_salary)
