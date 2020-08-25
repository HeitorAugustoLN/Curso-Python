nome = str(input("Digite seu nome completo: ")).strip()

nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
nomeSeparado = nome.split()
nomeTamanho = len(nome) - nome.count(' ')
primeiroNome = nomeSeparado[0]
primeiroNomeTamanho = len(nomeSeparado[0])


print("Analisando seu nome...")

print(f"Seu nome em maiusculo é {nomeMaiusculo}")
print(f"Seu nome em minusculo é {nomeMinusculo}")
print(f"Seu nome ao todo tem {nomeTamanho} letras")
print(f"Seu primeiro nome é {primeiroNome} e ele tem {primeiroNomeTamanho}")