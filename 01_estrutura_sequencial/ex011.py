"""
Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

- O produto do dobro do primeiro com metade do segundo.
- A soma do triplo do primeiro com o terceiro.
- O terceiro elevado ao cubo.
"""

primeiro_inteiro = int(input("Informe um valor inteiro: "))
segundo_inteiro = int(input("Informe um segundo valor inteiro: "))
valor_real = int(input("Informe um valor real: "))

print(
    f"O produto do dobro do primeiro com a metade do segundo: {(2 * primeiro_inteiro) * (segundo_inteiro / 2)}"
)
print(
    f"A soma do triplo do primeiro pelo terceiro: {(primeiro_inteiro * 3) + valor_real}"
)
print(f"O terceito elevado ao cubo: {valor_real * 3}")
