# Exercícios Python

# Mundo 1

O primeiro mundo foi pensando de forma a apresentar a linguagem ao aluno, o professor irá introduzir a linguagem, seus conceitos, montar o primeiro programa e ensinar alguns recursos básicos.

## Módulo 1 - Introdução ao Mundo da Programação

Nesse módulo não há exercícios!

## Módulo 2 - Primeiros passos com o Python

### Exercício 1

```python
print('Olá, mundo!')
```

### Exercício 2

```python
nome = input("Digite seu nome: ")
print(f"É um prazer te conhecer, {nome}!")
```

## Módulo 3 - Tratando dados e fazendo contas

### Exercício 3

```python
primeiroNumero = int(input("Digite um número: "))
segundoNumero = int(input("Digite outro número: "))
soma = primeiroNumero + segundoNumero

print(f"A soma entre {primeiroNumero} e {segundoNumero} resulta em {soma}")
```

### Exercício 4

```python
valor = input("Digite algo: ")

print(f"O tipo primitivo desse valor é {type(valor)}")
print(f"Só tem espaços? {valor.isspace()}")
print(f"É um número? {valor.isnumeric()}")
print(f"É alfabético? {valor.isalpha()}")
print(f"É alfanúmerico? {valor.isalnum()}")
print(f"Está em maiúsculas? {valor.isupper()}")
print(f"Está em minúsculas? {valor.islower()}")
print(f"Está capitalizada? {valor.istitle()}")
```

### Exercício 5

```python
numero = int(input("Digite um número: "))
antecessor = numero - 1
sucessor = numero + 1

print(
    f"Analisando o valor {numero}, seu antecessor é {antecessor} e o seu sucessor é"
    f" {sucessor}"
)
```
