from datetime import datetime

agora = datetime.now()
anoAtual = agora.year

anoNascimento = int(input("Ano de nascimento: "))
idade = anoAtual - anoNascimento

print(f"O atleta tem {idade} anos")

if idade <= 9:
    print("Classificação: MIRIM")
elif idade <= 14:
    print("Classificação: INFANTIL")
elif idade <= 19:
    print("Classificação: JÚNIOR")
elif idade <= 25:
    print("Classificação: SÊNIOR")
else:
    print("Classificação: MASTER")
