texto = str(input("Digite um texto: ")).replace(" ", "").upper()
reverso = texto[::-1]

print(f"O inverso de {texto} é {reverso}")
print("Temos um palíndromo" if texto == reverso else "O texto digitado não é um palíndromo")