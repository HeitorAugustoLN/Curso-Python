from random import randint

print("Vou pensar em um número de 0 a 5, tente advinhar!")

numeroUsuario = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")

numeroEscolhido = randint(0, 5)

if numeroUsuario == numeroEscolhido:
  print(f"Você... ACERTOU! Eu realmente escolhi {numeroEscolhido}")
else:
  print(f"Você... ERROU! Eu escolhi {numeroEscolhido} e você {numeroUsuario}")