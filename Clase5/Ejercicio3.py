numero_1 = float(input("Digite un numero 1 "))
numero_2 = float(input("Digite un numero 2 "))
numero_3 = float(input("Digite un numero 3 "))

if numero_1 > numero_2:
    if(numero_1 > numero_3):
        print("numero 1 es el mayor")
    else:
        print("numero 3 es el mayor")
else:
    if(numero_2 > numero_3):
        print("numero 2 es el mayor")
    else:
        print("numero 3 es el mayor")