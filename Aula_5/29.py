num = int(input("Digite um número inteiro: "))
if num % 5 == 0:
    if num >= 50:
        print("Multiplo Alto")
    else:
        print("Multiplo Baixo")
else:
    print("Não é múltiplo de 5.")