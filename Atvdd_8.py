a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
if a <= b and a <= c:
    if b <= c:
        print('Os números em ordem crescente são:', a, b, c)
    else:
        print('Os números em ordem crescente são:', a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print('Os números em ordem crescente são:', b, a, c)
    else:
        print('Os números em ordem crescente são:', b, c, a)
else:
    if a <= b:
        print('Os números em ordem crescente são:', c, a, b)
    else:
        print('Os números em ordem crescente são:', c, b, a)    