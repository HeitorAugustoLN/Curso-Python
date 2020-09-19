cedula50 = cedula20 = cedula10 = cedula1 = 0

print("=" * 53)
print("BANCO HALN".center(53))
print("=" * 53)

valor = int(input("Qual valor você quer sacar? R$"))

while valor > 0:
    if valor % 50 == 0:
        cedula50 += 1
        valor -= 50
    elif valor % 20 == 0:
        cedula20 += 1
        valor -= 20
    elif valor % 10 == 0:
        cedula10 += 1
        valor -= 10
    elif valor % 1 == 0:
        cedula1 += 1
        valor -= 1
print("=" * 53)
print(f"Total de {cedula50} cédulas de R$50")
print(f"Total de {cedula20} cédulas de R$20")
print(f"Total de {cedula10} cédulas de R$10")
print(f"Total de {cedula1} cédulas de R$1")
print("=" * 53)
print("Volte sempre ao BANCO HALN! Tenha um bom dia.")
