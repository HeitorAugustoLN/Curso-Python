from colored import fg

dividido = 0

numero = int(input("Digite um número: "))

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        dividido += 1
        print(f"{fg(10)}{divisor}{fg(15)}", end=" ")
        pass
    else:
        print(f"{fg(9)}{divisor}{fg(15)}", end=" ")
        pass
    pass
print(f"\nO número {numero} foi divisivel {dividido} vezes")
if dividido > 2:
    print("E por isso ele NÃO é PRIMO")
    pass
else:
    print("E por isso ele É PRIMO")
    pass
