from random import randint

print(
    """Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura"""
)

jogada = int(input("Qual é sua jogada? "))

if jogada > 2:
    print("Essa jogada não existe! Tente novamente.")
    exit(0)

computadorJogada = randint(0, 2)

print("JO")
print("KEN")
print("PO!!")

print("-=-=-=-=-=-=-=-=-=-=-=-=")
if jogada == 0:
    print("Jogador jogou pedra!")
elif jogada == 1:
    print("Jogador jogou papel!")
else:
    print("Jogador jogou tesoura")

if computadorJogada == 0:
    print("Computador jogou pedra!")
elif computadorJogada == 1:
    print("Computador jogou papel!")
else:
    print("Computador jogou tesoura")
print("-=-=-=-=-=-=-=-=-=-=-=-=")
if jogada != computadorJogada:
    if jogada == 0 and computadorJogada == 2:
        print("Jogador venceu!")
    elif jogada == 1 and computadorJogada == 0:
        print("Jogador venceu!")
    elif jogada == 2 and computadorJogada == 1:
        print("Jogador venceu!")
    else:
        print("Computador venceu!")
else:
    print("Empate!")