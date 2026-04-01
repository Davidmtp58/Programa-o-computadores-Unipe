#Leia dois números e exiba qual é o maior.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
if num1 > num2:
    print(num1, "é maior que", num2)
elif num1 < num2:
    print(num2, "é maior que", num1)