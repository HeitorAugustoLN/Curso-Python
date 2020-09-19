total = 0
maisDe1000 = 0
baratoNome = None
baratoPreço = None

print("-" * 53)
print("LOJA DO HEITOR".center(53))
print("-" * 53)
while True:
    produtoNome = str(input("Nome do produto: ")).strip()
    produtoPreço = float(input("Preço: R$"))

    total += produtoPreço

    if produtoPreço > 1000:
        maisDe1000 += 1

    if baratoNome == None:
        baratoNome = produtoNome
    else:
        if produtoPreço < baratoPreço:
            baratoNome = produtoNome
    if baratoPreço == None:
        baratoPreço = produtoPreço
    else:
        if produtoPreço < baratoPreço:
            baratoPreço = produtoPreço

    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

    if continuar == "N":
        break
print(" FIM DO PROGRAMA ".center(53, "-"))
print(f"O total da compra foi: R${round(total, 2)}")
print(f"Temos {maisDe1000} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {baratoNome} que custa R${baratoPreço}")