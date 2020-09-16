print("Gerador de PA")
primeiroTermo = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))

contador = 1
pa = primeiroTermo

while contador <= 10:
    print(pa, end=" ➡ ")
    pa += razao
    contador += 1
print("FIM")