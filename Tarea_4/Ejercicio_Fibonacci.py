def main():

    #Solicitamos un numero positivo al usuario
    numero = pedir_numero()
    
    
    print("\nEl termino " + str(numero) + " de la sucesion de Fibonacci es: " + str(calcular_sumatoria(numero)))

def pedir_numero():

    #Declaramos a esta variable como falsa para entrar al while
    es_positivo = False 

    #Verifica si los valores ingresados estan en los rangos establecidos
    while es_positivo == False:

        try:
            numero = int(input("Digite un numero positivo: "))
        except:
            print("El valor ingresado no es valido ")
        else: 
            #Verificamos que el numero sea positivo 
            if numero > 0:
                es_positivo = True 

    #Retornamos el numero ingresado por el usuario
    return numero 

#Calculamos el valor del termino en la posicion "numero"
def calcular_sumatoria(numero):

    contador = 0
    primer_numero = 0
    segundo_numero = 1 
    suma = 0 

    print("El termino 1 de la sucesion es: " + str(suma))

    if numero == 2:
        print("holaaaa")
        print("El termino 2 de la ssucesion es: " + str(segundo_numero)) 
        return segundo_numero

    #Comenzamos el while en contador + 2 pues tenemos dos condiciones iniciales
    while contador + 2 < numero :

        if contador == 0:
            print("El termino 2 de la sucesion es: " + str(segundo_numero))

        suma = primer_numero + segundo_numero

        primer_numero = segundo_numero 
        segundo_numero = suma 

        print("El termino " + str(contador + 3) + " de la sucesion es: " + str(suma) )
        contador+= 1 

    return suma



if __name__ == "__main__":
    main()
