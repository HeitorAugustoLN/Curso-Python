diasAlugados = int(input('Quantos dias alugados: '))
quilometrosRodados = float(input('Quantos km rodados: '))

preco = (diasAlugados * 60) + (quilometrosRodados * 0.15)

print(f'O total a pagar é de R${round(preco, 2)}')