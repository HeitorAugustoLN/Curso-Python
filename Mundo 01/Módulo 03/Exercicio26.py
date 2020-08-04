frase = str(input('Digite uma frase: ')).strip()
quantidadeDeA = frase.lower().count('a')
primeiroA = frase.lower().find('a') + 1
ultimoA = frase.lower().rfind('a') + 1

print(f"Nessa frase, apareceram {quantidadeDeA} A's")
print(f"O primeiro A apareceu no {primeiroA} caractere")
print(f"O último A apareceu no {ultimoA} caractere")