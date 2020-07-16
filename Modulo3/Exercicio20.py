from random import shuffle

primeiroAluno = str(input("Nome do primeiro aluno: "))
segundoAluno = str(input("Nome do segundo aluno: "))
terceiroAluno = str(input("Nome do terceiro aluno: "))
quartoAluno = str(input("Nome do quarto aluno: "))

lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
ordem = shuffle(lista)

print(f"A ordem de apresentação será: {lista}")
