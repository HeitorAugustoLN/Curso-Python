from math import hypot

catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print(f"A hipotenusa vai medir {round(hipotenusa, 2)}")
