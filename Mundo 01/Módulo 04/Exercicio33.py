primeiroNúmero = int(input("Primeiro número: "))
segundoNúmero = int(input("Segundo número: "))
terceiroNúmero = int(input("Terceiro número: "))

maiorNúmero = primeiroNúmero
if segundoNúmero > primeiroNúmero and segundoNúmero > terceiroNúmero:
	maiorNúmero = segundoNúmero
if terceiroNúmero > primeiroNúmero and terceiroNúmero > segundoNúmero:
	maiorNúmero = terceiroNúmero

menorNúmero = primeiroNúmero
if segundoNúmero < primeiroNúmero and segundoNúmero < terceiroNúmero:
	menorNúmero = segundoNúmero
if terceiroNúmero < primeiroNúmero and terceiroNúmero < segundoNúmero:
	menorNúmero = terceiroNúmero

print(f"O maior número é {maiorNúmero}")
print(f"O menor número é {menorNúmero}")