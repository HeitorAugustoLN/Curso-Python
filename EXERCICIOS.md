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

### Exercício 6

```python
numero = int(input("Digite um número: "))
dobro = numero * 2
triplo = numero * 3
raizQuadrada = numero ** 0.5

print(f"O dobro de {numero} vale {dobro}")
print(f"O tripo de {numero} vale {triplo}")
print(f"A raiz quadrada de {numero} é igual {raizQuadrada}")
```

### Exercício 7

```python
primeiraNota = float(input("Primeira nota do aluno: "))
segundaNota = float(input("Segunda nota do aluno: "))
media = (primeiraNota + segundaNota) / 2

print(f"A média entre {primeiraNota} e {segundaNota} é {media}")
```

### Exercício 8

```python
distancia = float(input("Digite uma distância em metros: "))

quilometros = distancia / 1000
hectometro = distancia / 100
decametro = distancia / 10
decimetro = distancia * 10
milimetro = distancia * 1000
centimetro = distancia * 100

print(f"A medida de {distancia}m corresponde a:")
print(f"{quilometros}km")
print(f"{hectometro}hm")
print(f"{decametro}dam")
print(f"{decimetro}dm")
print(f"{centimetro}cm")
print(f"{milimetro}mm")
```

### Exercício 9

```python
numero = int(input("Digite um número para ver sua tabuada: "))

print("------------")
print(f"{numero} × 1 = {numero * 1}")
print(f"{numero} × 2 = {numero * 2}")
print(f"{numero} × 3 = {numero * 3}")
print(f"{numero} × 4 = {numero * 4}")
print(f"{numero} × 5 = {numero * 5}")
print(f"{numero} × 6 = {numero * 6}")
print(f"{numero} × 7 = {numero * 7}")
print(f"{numero} × 8 = {numero * 8}")
print(f"{numero} × 9 = {numero * 9}")
print(f"{numero} × 10 = {numero * 10}")
print("------------")
```

### Exercício 10

```python
dinheiroEmReais = float(input("Quanto dinheiro você tem na carteira? R$"))
dinheiroEmDolar = dinheiroEmReais * 0.19

print(f"Com R${dinheiroEmReais} você pode comprar US${dinheiroEmDolar}")
```

### Exercício 11

```python
larguraParede = float(input("Largura da parede: "))
alturaParede = float(input("Altura da parede: "))

metrosQuadrados = larguraParede * alturaParede
quantidadeDeTinta = metrosQuadrados / 2

print(
    f"Sua parede tem a dimensão de {larguraParede} x {alturaParede} e sua área é de"
    f" {metrosQuadrados}m²."
)
print(f"Para pintar essa parede, você precisará de {quantidadeDeTinta}l de tinta.")
```

### Exercício 12

```python
preco = float(input("Qual é o preço do produto? R$"))
desconto = preco - (preco * 5 / 100)

print(
    f"O produto que custava R${preco}, na promoção com desconto de 5% vai custar"
    f" R${desconto}"
)
```

### Exercício 13

```python
salario = float(input("Qual é o salário do funcionário? R$"))
reajuste = salario + (salario * 15 / 100)

print(
    f"Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber"
    f" R${round(reajuste, 2)}"
)
```

### Exercício 14

```python
temperaturaCelsius = float(input("Informe a temperatura em °C: "))
temperaturaFahrenheit = (temperaturaCelsius * 9 / 5) + 32

print(
    f"A temperatura de {temperaturaCelsius}°C corresponde a {temperaturaFahrenheit}°F"
)
```

### Exercício 15

```python
diasAlugados = int(input("Quantos dias alugados: "))
quilometrosRodados = float(input("Quantos km rodados: "))

preco = (diasAlugados * 60) + (quilometrosRodados * 0.15)

print(f"O total a pagar é de R${round(preco, 2)}")
```

## Módulo 4 - Usando módulos no python

### Exercício 16

```python
from math import trunc

numero = float(input("Digite um valor: "))
numeroInteiro = trunc(numero)

print(f"O valor digitado foi {numero} e a sua porção inteira é {numeroInteiro}")
```

### Exercício 17

```python
from math import hypot

catetoOposto = float(input("Comprimento do cateto oposto: "))
catetoAdjacente = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print(f"A hipotenusa vai medir {round(hipotenusa, 2)}")
```

### Exercício 18

```python
from math import sin, cos, tan, radians

angulo = float(input("Digite algum ângulo: "))
seno = round(sin(radians(angulo)), 2)
cosseno = round(cos(radians(angulo)), 2)
tangente = round(tan(radians(angulo)), 2)

print(f"O ângulo {angulo} tem o SENO de {seno}")
print(f"O ângulo {angulo} tem o COSSENO de {cosseno}")
print(f"O ângulo {angulo} tem o TANGENTE de {tangente}")
```

### Exercício 19

```python
from random import choice

primeiroAluno = str(input("Nome do primeiro aluno: "))
segundoAluno = str(input("Nome do segundo aluno: "))
terceiroAluno = str(input("Nome do terceiro aluno: "))
quartoAluno = str(input("Nome do quarto aluno: "))

lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

alunoEscolhido = choice(lista)

print(f"O aluno escolhido foi {alunoEscolhido}")
```

### Exercício 20

```python
from random import shuffle

primeiroAluno = str(input("Nome do primeiro aluno: "))
segundoAluno = str(input("Nome do segundo aluno: "))
terceiroAluno = str(input("Nome do terceiro aluno: "))
quartoAluno = str(input("Nome do quarto aluno: "))

lista = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]
ordem = shuffle(lista)

print(f"A ordem de apresentação será: {lista}")
```

### Exercício 21

```python
from playsound import playsound

playsound("musica.mp3", True)
```

[Voltar](https://github.com/HeitorAugustoLN/python-course/blob/master/README.md)
