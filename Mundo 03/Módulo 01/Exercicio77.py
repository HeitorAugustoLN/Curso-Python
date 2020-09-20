palavras = (
    "aprender",
    "programar",
    "linguagem",
    "python",
    "curso",
    "gratis",
    "estudar",
    "praticar",
    "trabalhar",
    "mercado",
    "programador",
    "futuro",
)
for palavra in palavras:
    vogais = ""
    for letra in range(0, len(palavra)):
        if palavra[letra] in "aeiou":
            vogais += f"{palavra[letra]} "
            pass
        pass
    print(f"Na palavra {palavra.upper()} temos {vogais.strip()}")
    pass
