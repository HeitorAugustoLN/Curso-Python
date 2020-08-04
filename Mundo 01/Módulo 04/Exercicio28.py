from random import choice

print("Vou pensar em um número de 0 a 5, tente advinhar!")

numeroUsuario = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")

numeros = [0, 1, 2, 3, 4, 5]
numeroEscolhido = choice(numeros)

if numeroUsuario == numeroEscolhido:
  print(f"Você... ACERTOU! Eu realmente escolhi {numeroEscolhido}")
else:
  print(f"Você... ERROU! Eu escolhi {numeroEscolhido} e você {numeroUsuario}")