numeroTabuada = int(input("Digite um número para ver sua tabuada: "))

for numeroMultiplicacao in range(1, 11):
    resultado = numeroTabuada * numeroMultiplicacao
    print(f"{numeroTabuada} x {numeroMultiplicacao} = {resultado}")