a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
	print("Os segmentos acima PODEM FORMAR um triângulo")
else:
	print("Os segmentos acima NÃO PODEM FORMAR um triângulo")