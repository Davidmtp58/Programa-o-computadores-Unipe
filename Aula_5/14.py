#Leia um valor e: Converta para inteiro; Se for múltiplo de 3 → “Múltiplo de 3”; Senão → “Não é múltiplo”
num = input("Digite um número: ")
num_int = int(num)
if num_int % 3 == 0:
    print(num_int, "é múltiplo de 3.")
else:
    print(num_int, "não é múltiplo de 3.")