
#Declaramos la variable falsa para ingresar al while
es_positivo_1 = False

#Verificamos que el primer numero ingresado efectivamente sea mayor a 0 o bien positivo 
while es_positivo_1 == False:
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        es_positivo_1 = True
    else:
        print("Ingrese un numero positivo")


#Se declara en -1 pues asi siempre ingresa al while pues numero > 0 
numero_temporal = -1


#El while se termina una vez el usuario haya ingresado el mismo numero que ingreso por primera vez 
while numero_temporal != numero:


#Verificamos que los numeros ingresados por el usuario sean positivos
    es_positivo = False

    while es_positivo == False:
        numero_temporal= int(input("Ingrese un numero: "))
        if numero_temporal > 0:
            es_positivo = True
        else:
            print("Ingrese un numero positivo")


#Si es menor lo imprimimos
    if numero_temporal < numero:
        print(numero_temporal)
#Si es mayor se imprime "es mayor"
    elif numero_temporal > numero:
        print("Es mayor")

print("El programa ha terminado")

