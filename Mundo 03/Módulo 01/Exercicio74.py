from random import randint

menorNumero = None
maiorNumero = None

tupla = (
    randint(1, 9),
    randint(1, 9),
    randint(1, 9),
    randint(1, 9),
    randint(1, 9),
)

print(f"Os valores sorteados foram: {tupla}")

for numero in tupla:
    if menorNumero == None:
        menorNumero = numero
        pass
    else:
        if numero < menorNumero:
            menorNumero = numero
            pass
        pass
    if maiorNumero == None:
        maiorNumero = numero
        pass
    else:
        if numero > maiorNumero:
            maiorNumero = numero
            pass
        pass
    pass
print(f"O maior valor sorteado foi: {maiorNumero}")
print(f"O menor valor sorteado foi: {menorNumero}")
