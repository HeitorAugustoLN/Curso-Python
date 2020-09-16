continuar = "S"
maiorNumero = menorNumero = contador = soma = 0

while continuar == "S":
    numero = int(input("Digite um número: "))

    if menorNumero == 0:
        menorNumero = numero
    else:
        if numero < menorNumero:
            menorNumero = numero

    if maiorNumero == 0:
        maiorNumero = numero
    else:
        if numero > maiorNumero:
            maiorNumero = numero

    soma += numero
    contador += 1

    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / contador
print(f"Você digitou {contador} numeros e a media foi {media}")
print(f"O maior valor foi {maiorNumero} e o menor foi {menorNumero}")