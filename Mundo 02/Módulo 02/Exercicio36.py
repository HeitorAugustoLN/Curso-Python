valorCasa = float(input("Valor da casa: R$"))
salárioComprador = float(input("Salário do Comprador: R$"))
financiamentoAnos = int(input("Anos de financiamento: "))

máximoSalário = (salárioComprador * 30) / 100
pagamento = round(valorCasa / (financiamentoAnos * 12), 2)

print(
    f"Para pagar uma casa de R${round(valorCasa, 2)} em {financiamentoAnos} anos, a prestação será de R${round(pagamento, 2)}"
)
if pagamento <= máximoSalário:
    print("O emprestimo pode ser concedido!")
else:
    print("Emprestimo negado!")