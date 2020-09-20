numeros = (
    "zero",
    "um",
    "dois",
    "três",
    "quatro",
    "cinco",
    "seis",
    "sete",
    "oito",
    "nove",
    "dez",
    "onze",
    "doze",
    "treze",
    "catorze",
    "quinze",
    "dezesseis",
    "dezesete",
    "dezoito",
    "dezenove",
    "vinte",
)

while True:
    numero = int(input("Digite um número entre 0 e 20: "))
    if 0 <= numero <= 20:
        print(f"Você digitou o número {numeros[numero]}")

        continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
        while continuar not in "SN":
            continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
            pass
        if continuar == "N":
            break
        else:
            continue
        pass
    else:
        print("Tente novamente. ", end="")
        pass
