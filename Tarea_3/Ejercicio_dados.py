def main():

    #Creamos un arreglo con los valores ingresados por el jugador
    numeros = pedir_numeros()

    print(determinar_estado(numeros))


def pedir_numeros():
    #Declaramos esta variable como falsa para ingresar al while
    menores_a_6 = False

    #Verifica si los valores ingresados estan en los rangos establecidos
    while menores_a_6 == False:

        print("Recuerde que los valores ingresados deben estar en el intervalo [1,6]")
        try:
            numero_1 = int(input("Digite el valor del primer dado lanzado: "))
            numero_2 = int(input("Digite el valor del segundo dado lanzado: "))
            numero_3 = int(input("Digite el valor del tercer dado lanzado: "))
        except: 
            print("Algún valor ingresado no es valido")
        else:
            #Verificamos que los dados esten en el intervalo [1,6]
            if (numero_1 < 7 and numero_2 < 7 and numero_3 < 7 and numero_1 > 0 and numero_2 > 0 and numero_3 > 0):
                menores_a_6 = True

    #Creamos una lista con los numeros ingresados por el usuario
    return [numero_1, numero_2, numero_3]

#Verificamos cuantos 6 obtuvo el jugador
def determinar_estado(numeros):
    if numeros.count(6) == 3:
        return("El juego fue excelente")
    elif numeros.count(6) == 2:
        return("El juego fue muy bueno")
    elif numeros.count(6) == 1:
        return("El juego fue regular")
    else:
        return("El juego fue pesimo")

if __name__ == "__main__":
    main()