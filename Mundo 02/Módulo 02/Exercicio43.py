peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)

print(f"O IMC dessa pessoa é {imc}")
if imc < 18.5:
    print("Essa pessoa está abaixo do peso!")
elif imc < 25:
    print("Essa pessoa está no peso ideal.")
elif imc < 30:
    print("Essa pessoa está acima do peso ideal!")
elif imc < 40:
    print("Essa pessoa está obesa!")
else:
    print("Essa pessoa está em uma obesidade mórbida!")