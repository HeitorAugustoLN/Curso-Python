print("========== LOJINHA DO HEITOR ==========")
preço = float(input("Preço das compras: R$"))
print(
    """Formas de pagamento:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão"""
)

opção = int(input("Qual é a opção? "))
if opção == 1:
    total = preço - (preço * 0.1)
    print(f"Sua compra de R${preço}, vai custar R${total} no final")
elif opção == 2:
    total = preço - (preço * 0.05)
    print(f"Sua compra de R${preço}, vai custar R${total} no final")
elif opção == 3:
    total = preço
    valorParcelado = total / 2
    print(f"Sua compra será parcelada em 2x de R${valorParcelado} SEM JUROS")
    print(f"Sua compra de R${preço}, vai custar R${total} no final")
elif opção == 4:
    parcelas = int(input("Quantas parcelas? "))
    total = preço + (preço * 0.2)
    valorParcelado = total / parcelas
    if parcelas < 3:
        print("O mínimo dessa opção é 3 parcelas!!")
        print("Tente novamente!")
        exit(0)
    else:
        print(
            f"Sua compra será parcelada em {parcelas}x de R${round(valorParcelado, 2)} COM JUROS"
        )
        print(f"Sua compra de R${preço} vai custar R${total}")
else:
    print("Essa opção não existe!")
    print("Tente novamente!")
    exit(0)
print("Agradecemos sua prefêrencia! Tenha um bom dia.")