#Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles.
num = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num == num2:
    print("Os números são iguais.")
else:
    print("Os números são diferentes.")
    print("Diferença:", num - num2)