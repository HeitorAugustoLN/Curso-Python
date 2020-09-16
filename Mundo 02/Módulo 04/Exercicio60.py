numero = int(input("Digite um número para calcular seu fatorial: "))
contador = numero
fatorial = 1

print(f"Calculando {numero}! = ", end="")
while contador > 0:
    print(f"{contador}", end="")
    print(f" x " if contador > 1 else " = ", end="")
    fatorial *= contador
    contador -= 1
print(fatorial)