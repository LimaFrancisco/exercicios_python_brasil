# Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
from math import pi

raio_circulo = float(input("Informe o raio do circulo: "))
area_do_circulo = pi * (raio_circulo**2)

print(f"O raio do circulo é {area_do_circulo:.2f}")
