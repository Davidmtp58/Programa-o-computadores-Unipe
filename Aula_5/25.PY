#Leia um valor informado pelo usuário. Exiba o tipo da variável lida. Verifique se é possível converter o valor para número real (float). Se for possível, exiba o resultado da divisão desse número por 2. Caso contrário, exiba: “Não numérico”
valor = input("Digite um valor: ")
print("Tipo de variável:", type(valor))

try:
    numero = float(valor)
    print("Metade:", numero / 2)
except ValueError:
    print("Valor não numérico")