#Leia dois números informados pelo usuário. Se ambos forem positivos, calcule e exiba a soma entre eles. Caso contrário, calcule e exiba o produto entre eles.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
if num1 > 0 and num2 > 0:
    soma = num1 + num2
    print("A soma dos números é:", soma)
else:
    produto = num1 * num2
    print("O produto dos números é:", produto)