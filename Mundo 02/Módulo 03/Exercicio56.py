somaIdades = 0
homemVelhoIdade = 0
homemVelhoNome = ""
mulheresMenos20 = 0

for pessoa in range(1, 5):
    print(f"----- {pessoa}ª PESSOA -----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    somaIdades += idade

    if idade > homemVelhoIdade and sexo == "M":
        homemVelhoIdade = idade
        homemVelhoNome = nome
        pass

    if sexo == "F" and idade < 20:
        mulheresMenos20 += 1
        pass
    pass

mediaIdades = somaIdades / 4

print(f"A média de idade do grupo é de {mediaIdades} anos")
print(f"O homem mais velho tem {homemVelhoIdade} anos e se chama {homemVelhoNome}")
print(
    f"Ao todo são {mulheresMenos20} mulheres com menos de 20 anos"
    if mulheresMenos20 > 1
    else f"Ao todo há {mulheresMenos20} mulher com menos de 20 anos"
)
