# Faça um programa que peça as 4 notas bimestrais e mostre a média.

primeira_nota = float(input("Insira a primeira nota: "))
segunda_nota = float(input("Insira a segunda nota: "))
terceira_nota = float(input("Insira a terceira nota: "))
quarta_nota = float(input("Insira a quarta nota: "))

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

print(f"MEDIA = {media:.2f}")
