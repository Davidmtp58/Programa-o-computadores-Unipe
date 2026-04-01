#Leia um número e: Se for par e positivo → “Par positivo”; Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”
num = int(input("Digite um numero: "))
if num % 2 == 0 and num > 0:
    print('Par Positivo')
elif num % 2 == 0 and num < 0:
    print('Par Negativo')
else:
    print('Impar')