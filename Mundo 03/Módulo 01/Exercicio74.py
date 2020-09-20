from random import randint

tupla = (
    randint(1, 9),
    randint(1, 9),
    randint(1, 9),
    randint(1, 9),
    randint(1, 9),
)

maiorNumero = max(tupla)
menorNumero = min(tupla)

print(f"Os valores sorteados foram: {tupla}")
print(f"O maior valor sorteado foi: {maiorNumero}")
print(f"O menor valor sorteado foi: {menorNumero}")
