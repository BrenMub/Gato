#Declaramos la variable falsa para ingresar al while
es_positivo = False


#Verificamos si el numero ingresado es positivo
while es_positivo == False:
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        es_positivo = True
    else: 
        print("Ingrese un numero positivo")

numero_temporal = numero 

#Imprimimos desde el numero ingresado por el usuario hasta 1050
while numero_temporal <= 1050:
    print(numero_temporal)
    numero_temporal+=1

