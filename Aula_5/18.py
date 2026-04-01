#Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro.
num = float(input("Digite um número: "))
if num % 2 ==0 and num > 0:
    print("O número é par e positivo.")
elif num % 2 ==0 and num < 0:
    print("O número é par e negativo.")
elif num % 2 !=0 and num > 0:
    print("O número é ímpar e positivo.")
elif num % 2 !=0 and num < 0:
    print("O número é ímpar e negativo.")
else:
    print("O número é neutro.")