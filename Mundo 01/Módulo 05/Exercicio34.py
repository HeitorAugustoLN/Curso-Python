salário = float(input("Qual é o salário do funcionário? R$"))

if salário >= 1250:
	aumento = salário + ((salário * 10) / 100)
else:
	aumento = salário + ((salário * 15) / 100)

print(f"Quem ganhava R${salário} passa a ganhar R${round(aumento, 2)}")