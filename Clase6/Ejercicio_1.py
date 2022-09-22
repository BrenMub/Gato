numero_1 = int(input('Digite el primer numero: '))
numero_2 = int(input('Digite el segundo numero: '))
numero_3 = int(input('Digite el tercer numero: '))


if numero_1 == numero_2:
    if numero_2 == numero_3:
        print('Tres son iguales')
    else:
        print('Dos son iguales')
elif numero_2 == numero_3:
    print('Dos son iguales')
elif numero_1 == numero_3:
    print('Dos son iguales')
else:
    print('Ninguno es igual')
