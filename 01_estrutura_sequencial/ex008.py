# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_por_hora = float(input("Informe quanto você ganha por hora: "))
horas_trabalhadas = float(input("Informe o total de horas trabalhadas: "))

print(f"Você deve receber R$ {valor_por_hora * horas_trabalhadas:.2f}")
