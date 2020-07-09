salario = float(input('Qual é o salário do funcionário? R$'))
reajuste = salario + (salario * 15 / 100)

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${round(reajuste, 2)}')