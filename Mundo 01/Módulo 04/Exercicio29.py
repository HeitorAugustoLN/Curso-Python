velocidadeDoCarro = float(input("Qual é a velocidade atual do carro? "))

if velocidadeDoCarro > 80.0:
  multa = round((velocidadeDoCarro - 80.0) * 7.0, 2)
  print(f"Você ultrapassou o limite de velocidade! Você vai pagar R${multa}")
print("Tenha um bom dia e dirija com segurança")