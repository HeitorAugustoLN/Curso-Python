primeiroNumero = int(input("Primeiro valor: "))
segundoNumero = int(input("Segundo valor: "))

while True:
    escolha = int(
        input(
            """[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa

> Qual é sua opção? """
        )
    )
    if escolha == 1:
        soma = primeiroNumero + segundoNumero
        print(f"A soma entre {primeiroNumero} e {segundoNumero} é {soma}")
    elif escolha == 2:
        produto = primeiroNumero * segundoNumero
        print(
            f"O produto da multiplicação de {primeiroNumero} e {segundoNumero} é {produto}"
        )
    elif escolha == 3:
        maiorNumero = primeiroNumero
        if segundoNumero > primeiroNumero:
            maiorNumero = segundoNumero

        print(
            f"O maior número entre {primeiroNumero} e {segundoNumero} é {maiorNumero}"
        )
    elif escolha == 4:
        print("Informe os números novamente:")

        primeiroNumero = int(input("Primeiro valor: "))
        segundoNumero = int(input("Segundo valor: "))
    elif escolha == 5:
        exit()
    else:
        print("Essa opção não existe!")
