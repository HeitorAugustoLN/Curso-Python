primeiraNota = float(input("Primeira nota: "))
segundaNota = float(input("Segunda nota: "))
media = (primeiraNota + segundaNota) / 2

print(f"Tirando {primeiraNota} e {segundaNota}, a média do aluno é {media}")
if media < 5.0:
    print("O aluno foi REPROVADO")
elif media >= 5.0 and media < 7.0:
    print("O aluno está na RECUPERAÇÃO")
else:
    print("O aluno está APROVADO")