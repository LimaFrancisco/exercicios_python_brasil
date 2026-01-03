"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

area = float(input("Informe a area em metros do local a ser pintado: "))
if area > 3:
    quantidade = area // 3
    if area % 3 != 0:
        quantidade = quantidade + 1
    print(f"Quantidade de latas: {quantidade:.0f}")
    print(f"Preço: R$ {quantidade * 80:.2f}")

else:
    print("Quantidade de latas: 1")
    print("Preço: R$ 80,00")
