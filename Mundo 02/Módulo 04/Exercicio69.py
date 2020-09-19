mulheres20 = homensCadastrados = maioridade = 0

while True:
	print("-" * 53)
	print("CADASTRE UMA PESSOA".center(53))
	print("-" * 53)

	idade = int(input("Idade: "))
	sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]

	while sexo not in "MF":
		sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]

	print("-" * 53)

	if sexo == "M":
		homensCadastrados += 1
	if idade > 18:
		maioridade += 1
	if sexo == "F" and idade < 20:
		mulheres20 += 1

	continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
	while continuar not in "SN":
		continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]

	if continuar == "N":
		break
print(f"Total de pessoas com mais de 18 anos: {maioridade}")
print(f"Ao todo temos {homensCadastrados} homens cadastrados")
print(f"E temos {mulheres20} mulheres com menos de 20 anos")
