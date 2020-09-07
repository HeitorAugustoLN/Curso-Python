soma = 0
contagem = 0

for valor in range(1, 7):
    numero = int(input(f"Digite o valor {valor}: "))
    if numero % 2 == 0:
        soma += numero
        contagem += 1
        pass
    pass
print(f"Você informou {contagem} pares e a soma foi {soma}")
