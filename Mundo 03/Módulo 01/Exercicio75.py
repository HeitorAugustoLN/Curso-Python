primeiroValor = int(input("Digite um número: "))
segundoValor = int(input("Digite outro número: "))
terceiroValor = int(input("Digite mais um número: "))
quartoValor = int(input("Digite o último número: "))

tupla = (primeiroValor, segundoValor, terceiroValor, quartoValor)
quantidade9 = tupla.count(9)

print(f"Você digitou os valores: {tupla}")
print(f"O valor 9 apareceu {quantidade9} vezes")
if tupla.count(3) > 0:
    posicao3 = tupla.index(3) + 1
    print(f"O valor 3 apareceu na {posicao3}° posição")
else:
    print("O valor 3 não apareceu nenhuma vez")
print(f"Os valores pares digitados foram ", end="")
for numero in tupla:
    if numero % 2 == 0:
        print(numero, end=" ")
