def main():

    #Solicitamos un numero al usuario
    numero = pedir_numero()

    print("\nEl numero digitado por el usuario es " + str(numero) + " y su factorial es: " + str(calcular_factorial(numero)))

def pedir_numero():

    #Declaramos esta variable como verdadera para ingresar al while
    es_negativo = True 

    #Verifica si los valores ingresados estan en los rangos establecidos
    while es_negativo == True:

        try:
            numero = int(input("Digite un numero mayor o igual que 0: "))
        except:
            print("El valor ingresado no es valido ")
        else: 
            #Verificamos que el numero no sea negativo
            if numero >= 0:
                es_negativo = False 

    #Retornamos el numero ingresado por el usuario
    return numero 

#Calculamos el factorial 
def calcular_factorial(numero):

    contador = 1
    productoria = 1

    print("El factorial de 0 es: " + str(productoria))


    while contador <= numero :
        productoria = productoria*contador
        print("El factorial de " + str(contador) + " es: " + str(productoria))
        contador += 1
    
    return productoria 

if __name__ == "__main__":
    main()