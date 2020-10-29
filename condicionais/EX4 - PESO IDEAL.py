h = float(input('Informe a altura: '))
sex = input('Informe o sexo: Masculino/Feminino: ')

if sex == 'Masculino':
    print('O peso ideal é: {}' .format(72.7*h - 58))
elif sex == 'Feminino':
    print('O peso ideal é: {}' .format(62.1*h - 44.7))
else:
    print('Sexo informado é inválido')
    
