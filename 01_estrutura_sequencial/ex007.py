# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado_do_quadrado = float(input("Informe o tamanho do lado do quadrado: "))
area_do_quadrado = lado_do_quadrado**2
print(
    f"A area do quadrado é {area_do_quadrado} e o dobro dessa area é {area_do_quadrado * 2}"
)
