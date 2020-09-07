menor = None
maior = None

print("=" * 30)
for pessoa in range(1, 6):
    peso = float(input(f"Peso da {pessoa}ª pessoa: "))

    if maior == None:
        maior = peso
        pass
    elif menor == None:
        menor = peso
        pass
    elif peso > maior:
        maior = peso
        pass
    elif peso < menor:
        menor = peso
        pass
    pass
print("=" * 30)
print(f"Menor: {menor}kg")
print(f"Maior: {maior}kg")
print("=" * 30)