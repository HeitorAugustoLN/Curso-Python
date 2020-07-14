from math import sin, cos, tan, radians

angulo = float(input("Digite algum ângulo: "))
seno = round(sin(radians(angulo)), 2)
cosseno = round(cos(radians(angulo)), 2)
tangente = round(tan(radians(angulo)), 2)

print(f"O ângulo {angulo} tem o SENO de {seno}")
print(f"O ângulo {angulo} tem o COSSENO de {cosseno}")
print(f"O ângulo {angulo} tem o TANGENTE de {tangente}")
