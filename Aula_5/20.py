#Leia um valor e: verifique se eles está entre 0 e 100, caso o número esteja fora do intervalo, mostre na tela o valor
num = float(input("Digite um número: "))
if 0 <= num <= 100:
    print("O número está entre 0 e 100.")
else:
    print("O número está fora do intervalo. Valor:", num)