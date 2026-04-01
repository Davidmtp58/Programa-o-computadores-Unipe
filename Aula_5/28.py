#Leia um valor informado pelo usuário. Verifique o tipo da variável; Caso seja possível interpretá-lo como um valor numérico: Se for um número inteiro, exiba o dobro; Caso seja um número real, exiba a metade; Caso não seja possível interpretar como número, exiba: “Tipo inválido”.
valor = input("Digite um valor: ")
print("Tipo da variável:", type(valor))
try:
    num=float(valor)
    if num == int(num):
        print("Dobro:", num*2)
    else:
        print("Metade:", num/2)
except ValueError:
    print("Tipo inválido")