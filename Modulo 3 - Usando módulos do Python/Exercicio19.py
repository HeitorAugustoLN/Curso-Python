from random import choice

primeiroAluno = str(input("Nome do primeiro aluno: "))
segundoAluno = str(input("Nome do segundo aluno: "))
terceiroAluno = str(input("Nome do terceiro aluno: "))
quartoAluno = str(input("Nome do quarto aluno: "))

lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

alunoEscolhido = choice(lista)

print(f"O aluno escolhido foi {alunoEscolhido}")