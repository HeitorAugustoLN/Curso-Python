listagemPreco = (
    "Frango",
    23.4,
    "Pão",
    12.75,
    "Picanha",
    60.3,
    "Arroz",
    40,
    "Feijão",
    12,
)

nome = 0
preco = 1

for item in range(0, len(listagemPreco)):
    if item % 2 == 0:
        print(f"{listagemPreco[item]:.<30}", end="")
        pass
    else:
        print(f"R${listagemPreco[item]:>7.2f}")
