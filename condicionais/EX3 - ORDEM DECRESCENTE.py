n1 = int(input('Informe um valor: '))
n2 = int(input('Informe um valor diferente de {}: ' .format(n1)))

if n1 > n2:
    print(n1, n2)
elif n2 > n1:
    print(n2, n1)
else:
    print('Os dois valores são iguais')
