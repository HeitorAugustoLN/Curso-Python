numero = int(input("Digite um número inteiro: "))

print("Escolha uma das bases de conversão:")
print("[ 1 ] converter para binário")
print("[ 2 ] converter para octal")
print("[ 3 ] converter para hexadecimal")

escolha = int(input("Sua opção: "))

if escolha == 1:
    print(f"{numero} convertido para binário é {bin(numero)[2:]}")
elif escolha == 2:
    print(f"{numero} convertido para octal é {oct(numero)[2:]}")
elif escolha == 3:
    print(f"{numero} convertido para hexadecimal é {hex(numero)[2:]}")
else:
    print("Esse número não está na lista, execute o programa novamente")