#Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
soma = num1 + num2
print("A soma de", num1, "e", num2, "é", soma)
if num1 > num2:
    print(num1, "é maior que", num2)
elif num1 < num2:
    print(num2, "é maior que", num1)
else:
    print("Os números são iguais.")