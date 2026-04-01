# Leia um número e: Se for maior que 100 → mostre metade; Senão → mostre o dobro.
num = float(input("Digite um número: "))
if num > 100:
    metade = num / 2
    print("A metade de", num, "é", metade)
else:
    dobro = num * 2
    print("O dobro de", num, "é", dobro)