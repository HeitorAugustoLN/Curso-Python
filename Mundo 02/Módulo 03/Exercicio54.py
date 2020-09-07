from datetime import datetime

anoAtual = datetime.now().year
maiores = 0
menores = 0

print("=" * 37)
for pessoa in range(1, 8):
    nascimento = int(input(f"Em que ano a {pessoa}ª pessoa nasceu? "))
    if anoAtual - nascimento >= 21:
        maiores += 1
        pass
    else:
        menores += 1
        pass
    pass
print("=" * 37)
print(f"Menores de idade: {menores}")
print(f"Maiores de idade: {maiores}")
print("=" * 37)