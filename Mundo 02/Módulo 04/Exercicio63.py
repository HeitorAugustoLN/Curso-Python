print("-" * 45)
print("Sequência de Fibonacci")
print("-" * 45)
termos = int(input("Quantos termos você quer mostrar? "))
primeiroTermo = 0
segundoTermo = 1
print("=" * 45)
print(f"{primeiroTermo} ➡ {segundoTermo}", end=" ➡ ")
contador = 3
while contador <= termos:
    fibonacci = primeiroTermo + segundoTermo
    print(fibonacci, end=" ➡ ")
    primeiroTermo = segundoTermo
    segundoTermo = fibonacci
    contador += 1
print("FIM")
print("=" * 45)