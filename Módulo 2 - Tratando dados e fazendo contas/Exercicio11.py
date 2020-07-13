larguraParede = float(input("Largura da parede: "))
alturaParede = float(input("Altura da parede: "))

metrosQuadrados = larguraParede * alturaParede
quantidadeDeTinta = metrosQuadrados / 2

print(
    f"Sua parede tem a dimensão de {larguraParede} x {alturaParede} e sua área é de"
    f" {metrosQuadrados}m²."
)
print(f"Para pintar essa parede, você precisará de {quantidadeDeTinta}l de tinta.")
