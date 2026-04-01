#Leia um valor e verifique: Se é maior que 10 → “Maior que 10”; Caso contrário → “Menor ou igual a 10”.
num = int(input("Digite um número: "))
if num > 10:
    print("Maior que 10")
elif num == 10:
    print("Igual a 10")
else:
    print("Menor que 10")