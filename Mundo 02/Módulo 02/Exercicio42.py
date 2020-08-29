a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))

if a < b + c and b < a + c and c < a + b:
    if a == b == c == a:
        print("Os segmentos podem formar um triângulo equilátero")
    elif a != b != c != a:
        print("Os segmentos podem formar um triângulo escaleno")
    else:
        print("Os segmentos podem formar um triângulo isósceles")
else:
    print("Os segmentos não podem formar um triângulo")