distanciaViagem = float(input("Qual é a distancia da sua viagem? "))

if distanciaViagem <= 200:
  preco = distanciaViagem * 0.50
else:
  preco = distanciaViagem * 0.45

print(f"Você está prestes a começar uma viagem de {round(distanciaViagem)}km")
print(f"O preço da sua passagem será R${round(preco, 2)}")