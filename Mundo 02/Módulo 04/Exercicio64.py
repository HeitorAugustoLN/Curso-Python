numero = contador = soma = 0
numero = int(input("Digite um número [999 para parar]: "))
while numero != 999:
    contador += 1
    soma += numero
    numero = int(input("Digite um número [999 para parar]: "))

print(f"Você digitou {contador} números e a soma entre eles foi: {soma}")