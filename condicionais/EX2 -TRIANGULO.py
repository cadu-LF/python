# Carlos Eduardo Ferreira
# 22594


l1 = float(input('Informe o valor do lado 1 do triângulo: '))
l2 = float(input('Informe o valor do lado 2 do triângulo: '))
l3 = float(input('Informe o valor do lado 3 do triângulo: '))

if ((l1 < l2 + l3) and (l2 < l3 + l1) and (l3 < l1 + l2)):
#    if ((l1 == l2) and (l2 == l3)):
     if l1 == l2 == l3:
        print('Triângulo equilátero')
    elif ((l1 == l2) or (l1 == l3) or (l2 == l3)):
        print('Triângulo isóceles')
    else:
        print('Triângulo escaleno')
else:
    print('Não é triângulo')
        
