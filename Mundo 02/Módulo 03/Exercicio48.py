soma = 0
quantidade = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        soma += numero
        quantidade += 1
    pass

print(f"A soma de todos os {quantidade} valores solicitados é {soma}")