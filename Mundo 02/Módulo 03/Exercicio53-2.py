texto = str(input("Digite um texto: ")).replace(" ", "").upper()
inverso = ""

for letra in range(len(texto) - 1, -1, -1):
    inverso += texto[letra]

print(f"O inverso de {texto} é {inverso}")
print("Temos um palíndro" if texto == inverso else "O texto digitado não é um palíndromo")