nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.split()
primeiroNome = nomes[0]
ultimoNome = nomes[len(nomes) - 1]

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiroNome}')
print(f'Seu ultimo nome é {ultimoNome}')