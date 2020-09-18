while True:
	tabuada = int(input("Quer ver a tabuada de qual valor? "))
	if tabuada < 1:
		break
	else:
		for numeroAtual in range(1, 11):
			resultado = tabuada * numeroAtual
			print(f"{tabuada} x {numeroAtual} = {resultado}")
