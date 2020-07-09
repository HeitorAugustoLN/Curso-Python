distancia = float(input('Digite uma distância em metros: '))

quilometros = distancia / 1000
hectometro = distancia / 100
decametro = distancia / 10
decimetro = distancia * 10
milimetro = distancia * 1000
centimetro = distancia * 100

print(f'A medida de {distancia}m corresponde a:')
print(f'{quilometros}km')
print(f'{hectometro}hm')
print(f'{decametro}dam')
print(f'{decimetro}dm')
print(f'{centimetro}cm')
print(f'{milimetro}mm')
