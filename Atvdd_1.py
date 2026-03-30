# Recebe dois números
#n1 = float(input('Digite um numero:'))
#n2 = float(input('Digite um numero:'))

#resultado = n1 * n2

#print("O resultado da operação é:", resultado)
#a = int(input('Digite um numero:'))
#b = int(input('Digite um numero:'))
#c = int(input('Digite um numero:'))
#if a > b and a > c:
#    print('O maior numero é:', a)
#elif b > a and b > c:
#    print('O maior numero é:', b)
#else:    print('O maior numero é:', c)
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

if a == b == c:
    print('Os três números são iguais')
elif a == b and a > c:
    print('A e B são iguais e são os maiores:', a)
elif a == c and a > b:
    print('A e C são iguais e são os maiores:', a)
elif b == c and b > a:
    print('B e C são iguais e são os maiores:', b)
elif a > b and a > c:
    print('O maior número é:', a)
elif b > a and b > c:
    print('O maior número é:', b)
else:
    print('O maior número é:', c)
