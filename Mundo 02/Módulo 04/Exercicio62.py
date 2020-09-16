print("Gerador de P.A")
print("=-" * 10)

primeiroTermo = int(input("Primeiro termo: "))
razaoPA = int(input("Razão da PA: "))

termos = 10
pa = primeiroTermo

while termos > 0:
    print(pa, end=" ➡ ")
    pa += razaoPA
    termos -= 1
    if termos == 0:
        print("PAUSA")
        termos = int(input("Quantos termos você quer mostrar a mais? "))
        continue