soma = contador = 0

while True:
	numero = int(input("Digite um número [999 para parar]: "))
	if numero == 999:
		break
	else:
		soma += numero
		contador += 1
print(f"Foram {contador} numeros digitados e a soma entre eles foi {soma}")
