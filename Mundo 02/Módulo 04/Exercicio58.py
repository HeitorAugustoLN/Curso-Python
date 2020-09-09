from random import randint

print("Sou seu computador...")

computador = randint(0, 10)

print("Acabei de pensar em número entre 0 e 10")
print("Será que você consegue adivinhar qual foi?")

tentativas = 1

palpite = int(input("Qual é seu palpite? "))
while palpite != computador:
	tentativas += 1
	if computador > palpite:
		print("Mais... Tente mais uma vez.")
	else:
		print("Menos... Tente mais uma vez.")
	palpite = int(input("Qual é seu palpite? "))
print(f"Acertou com {tentativas} tentativas. Parabéns!")
