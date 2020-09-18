from random import randint

perdeu = False
while True:
	if perdeu == True:
		break
	else:
		print("=-" * 35)
		print("VAMOS JOGAR PAR OU IMPAR!")
		print("=-" * 35)

		jogadorValor = int(input("Diga um valor: "))
		jogadorPalpite = str(input("Par ou impar? [P/I] ")).strip().upper()[0]
		computadorValor = randint(0, 10)
		resultado = jogadorValor + computadorValor

		print("-" * 70)
		
		if resultado % 2 == 0:
			print(f"Você jogou {jogadorValor} e o computador {computadorValor}. O total deu {resultado}, esse valor é PAR!")

			if jogadorPalpite == "P":
				print("Você venceu!")
				print("Vamos jogar novamente...")

				perdeu = False
			elif jogadorPalpite == "I":
				print("Você perdeu!")
				perdeu = True
			else:
				print("Esse valor não existe! Tente novamente...")
		else:
			print(f"Você jogou {jogadorValor} e o computador {computadorValor}. O total deu {resultado}, esse valor é IMPAR!")

			if jogadorPaplite == "I":
				print("Você venceu!")
				print("Vamos jogar novamente...")

				perdeu = False
			elif jogadorPalpite == "P":
				print("Você perdeu!")
				perdeu = True
			else:
				print("Esse valor não existe! Tente novamente...")
