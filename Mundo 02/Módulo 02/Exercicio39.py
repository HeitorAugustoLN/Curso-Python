import datetime

agora = datetime.datetime.now()
anoAtual = agora.year
anoNascimento = int(input("Ano de nascimento: "))
idade = anoAtual - anoNascimento

print(f"Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}")

if idade < 18:
    print(f"Ainda faltam {(anoNascimento + 18) - anoAtual} anos para o alistamento")
    print(f"Seu alistamento será em {anoAtual + idade}")
elif idade > 18:
    print(
        f"Você deveria ter se alistado há {anoAtual - (anoNascimento - (idade - 18))} anos"
    )
    print(f"Seu alistamento foi em {anoNascimento - (idade - 18)}")
else:
    print("Você tem que se alistar imediatamente")