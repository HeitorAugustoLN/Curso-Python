timesBrasileiros = (
    "Internacional",
    "Atlético-MG",
    "São Paulo",
    "Vasco da Gama",
    "Flamengo",
    "Palmeiras",
    "Santos",
    "Fluminense",
    "Ceará SC",
    "Fortaleza",
    "Corinthians",
    "Atlético-GO",
    "Grêmio",
    "Athletico-PR",
    "Sport Recife",
    "Bahia",
    "Botafogo",
    "Goiás",
    "Coritiba",
    "Bragantino-SP",
)
print(f"Lista de times do Brasileirão: {timesBrasileiros}")
print("-" * 53)
print(f"Os 5 primeiros são {timesBrasileiros[:6]}")
print("-" * 53)
print(f"Os 4 últimos são {timesBrasileiros[16:]}")
print("-" * 53)
print(f"Times em ordem alfabética {sorted(timesBrasileiros)}")
print("-" * 53)
print(f"O time do goiás está na {timesBrasileiros.index('Goiás')}° posição")
