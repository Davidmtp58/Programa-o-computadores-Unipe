#Leia um valor e: Mostre o tipo; Se for numérico (após conversão) → mostre o quadrado.
Valor = (input("Digite um número: "))
valor = input("Digite um valor: ")
print("Tipo da variável:", type(valor))

try:
    numero = float(valor)
    quadrado = numero ** 2
    print("Quadrado:", quadrado)
except:
    print("Valor não numérico")