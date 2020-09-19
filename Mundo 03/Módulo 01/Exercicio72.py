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

numeroInput = int(input("Digite um número entre 0 a 20: "))
while numeroInput < 0 or numeroInput > 20:
    numeroInput = int(input("Tente novamente! Digite um número entre 0 a 20: "))
    pass

print(f"Você digitou o número {numeros[numeroInput]}")
