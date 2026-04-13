excelente = 0
ruim = 0

for i in range(50):
    print(f"\nEntrevistado {i+1}")

    nome = input("Nome: ")
    idade = int(input("Idade: "))

    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\nResultado final:")
print("EXCELENTE:", excelente)
print("RUIM:", ruim)
