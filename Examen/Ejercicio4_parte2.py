#Solicitamos un numero de al menos 6 cifras
numero = int(input("Digite un numero de al menos 6 cifras: "))

numero_temporal = numero
contador_pares = 0
contador_impares = 0 

#El while se termina una vez ya hayamos terminado de contar los digitos, es decir, cuando la parte entera es 0
while numero_temporal!= 0:

    #Si es par aumentamos el contador de pares
    if numero_temporal%2 == 0:
        contador_pares += 1
        
    #Sino aumentamos el de impares 
    else:
        contador_impares += 1

    numero_temporal = numero_temporal//10


print("El numero ingresado tiene " + str(contador_pares) + " numeros pares " + "y tiene " + str(contador_impares) + " numeros impares")


