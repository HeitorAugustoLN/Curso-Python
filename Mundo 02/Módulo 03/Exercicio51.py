print("=" * 33)
print("     10 Termos de uma P.A.       ")
print("=" * 33)
termo = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
decimo = termo + (10 - 1) * razao
print("=" * 33)
for PAs in range(termo, decimo + razao, razao):
    print(PAs, end=" → ")
    pass
print("ACABOU!")
