numero_1 = int(input('Digite el primer numero: '))
numero_2 = int(input('Digite el segundo numero: '))
numero_3 = int(input('Digite el tercer numero: '))

if numero_1 > numero_2:
    print('a')
    if numero_1 > numero_3:
        if numero_2 > numero_3:
            print(numero_2)
        else:
            print('espacio')
            print(numero_3)
    else:
        print('entreee')
        print(numero_1)
elif numero_1 > numero_3:
    print('b')
    if numero_3 > numero_2:
        print(numero_3)
    else:
        print(numero_1)
elif numero_3 > numero_2:
    print('c')
    if numero_2 > numero_1:
        print(numero_2)
    else:
        print(numero_1)