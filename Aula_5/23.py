#Leia três números inteiros informados pelo usuário. Exiba em ordem decrescente o resto da divisão por 3. 
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

r1 = n1 % 3
r2 = n2 % 3
r3 = n3 % 3

if r1 >= r2 and r1 >= r3:
    if r2 >= r3:
        print(r1, r2, r3)
    else:
        print(r1, r3, r2)

elif r2 >= r1 and r2 >= r3:
    if r1 >= r3:
        print(r2, r1, r3)
    else:
        print(r2, r3, r1)

else:
    if r1 >= r2:
        print(r3, r1, r2)
    else:
        print(r3, r2, r1)
