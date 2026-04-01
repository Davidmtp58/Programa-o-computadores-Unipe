#Leia um número inteiro. Verifique se ele está no intervalo de 1 a 100 (inclusive). Se estiver: Verifique se o número é par ou ímpar; Exiba: “Par no intervalo” ou “Ímpar no intervalo”. Caso não esteja no intervalo, exiba: “Fora do intervalo”.
num = int(input("Digite um número inteiro: "))
if num >=1 and num <=100:
    if num % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
else:
    print("O número não está entre o intervalo 1 e 100.")