#Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe “Número inválido”
num = int(input("Digite um número: "))
if num > 0:
    print("Positivo")
    raiz = num ** 0.5
    print("A raiz aproximada de", num, "é", raiz)
elif num < 0:
    print("Número inválido")