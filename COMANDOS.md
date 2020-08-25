# Comandos Python

```python
# Comandos gerais

print(mensagem) # Escreve algo na tela
input(mensagem) # Pede para o usúario uma entrada (resposta)

# Tipos primitivos

type(variavel) # Verificar tipo

int(variavel) # Número inteiro
bool(variavel) # Verdadeiro ou falso (Valor boleano [Binário])
str(variavel) # Mensagem
float(variavel) # Número quebrado (não inteiro)

# Operadores aritméticos

*  # Multiplicação
+  # Soma
-  # Subtração
/  # Divisão
** # Potência
// # Divisão inteira
%  # Resto da divisão

# Operadores aritméticos - Ordem de procedência

# () 
# **
# * / // %
# + -

# Comandos verificadores de string

variavelString.isspace() # Verifica se é um espaço
variavelString.isnumeric() # Verifica se há apenas números
variavelString.isalpha() # Verifica se há apenas letras
variavelString.isalnum() # Verifica se há letras e números
variavelString.isupper() # Verifica se a palavra inteira está em maiusculo
variavelString.islower() # Verifica se a palavra inteira está em minusculo
variavelString.istitle() # Verifica se está capitalizada

# Módulo: math

math.trunc(numero) # Retorna apenas o valor inteiro

math.hypot(cateto, cateto) # Retorna a hipotenusa dos catetos

math.sin(angulo) # Retorna o seno do angulo
math.cos(angulo) # Retorna o cosseno do angulo
math.tan(angulo) # Retorna o tangente do angulo
math.radians(graus) # Retorna o grau do angulo para radianos

# Módulo: random

random.choice(array) # Escolhe um item do array
random.shuffle(array) # Mistura o array
random.randint(numero, numero) # Escolhe um numero aleatório entre os numeros selecionados

# Módulo: playsound

playsound.playsound(caminho/para/o/arquivo) # Toca um arquivo de audio

# Fatiamento de strings

variavelString[numero] # Escreve o caractere que está no indice do numero indicado
variavelString[numero:numero] # Escreve os caracteres que estão entre os números indicados 
# Começando pelo primeiro numero e terminando pelo indice antes do ultimo número
variavelString[numero:numero:numero] # # Escreve os caracteres que estão entre os números indicados pulando a quantidade indicada do terceiro nome
variavelString[:numero] # Escreve do começo da string até o indice indicado
variavelString[numero:] # Escreve do indice indicado até o final da string
variavelString[numero::numero] # Escreve do indice indicado até o final da string pulando a quantidade indicada no último numero

# Analise de strings

len('string') # Mostra o comprimento da string

variavelString.count('string') # Irá contar quantos caracteres iguais ao da string indicada tem na variavel
variavelString.count('string', numero, numero) # Ele irá contar quantos caracteres iguais ao da string indicada tem na variavel com fatiamento dos numeros indicados

variavelString.find('string') # Irá encontrar os caracteres da string na variavel e irá mostrar onde ele começou
variavelString.rfind('string') # Irá encontrar os caracteres da string na variavel a partir da direita (fim) e irá mostrar onde os caracterrs foram encontrados
# Se colocar uma string inexistente na variavel ele irá retornar -1
'string' in variavelString # Verifica se existe a string na variavel

# Transformações de strings

variavelString.replace('string', 'string') # Irá trocar a primeira string na variavel (existe na variavel) pela segunda string (não existe na variavel)
variavelString.upper() # Fará que todo caractere da variavel seja maiusculo
variavelString.lower() # Fará que todo caractere da variavel seja minusculo
variavelString.capitalize() # Fará que apenas o primeiro caractere da variavel seja maiusculo sendo assim o resto dos caracteres fica em minusculo
variavelString.title() # Fará que todo primeiro caractere de cada palavra fique maiusculo
variavelString.strip() # Removerá todos os espaços excedentes no inicio e no fim da variavel
variavelString.rstrip() # Removerá todos os espaços excedentes da direita (fim)
variavelString.lstrip() # Removerá todos os espaços excedentes da esquerda (começo)

# Divisão de strings

variavelString.split() # Irá separar os espaços da variavel fazendo um array
# Se quiser separar algo especifico, é só colocar dentro dos parentes entre aspas

# Junção de strings

'string'.join(variavelString) # Irá juntar o que foi separado
# Se quiser juntar coisas especificas é só colocar dentro dos parentes entre aspas

# Condição simples
if condicao:
  bloco True

# Condição composta
if condicao:
  bloco True
else:
  bloco False

# Condição simplificada
print('objeto novo' if tempo <= 4 else 'objeto velho')

if condicao and condicao:
	bloco True

if condicao and condicao:
	bloco True
else:
	bloco False

if condicao or condicao:
	bloco True

if condicao or condicao:
	bloco True
else:
	bloco False
```

[Voltar](README.md)
