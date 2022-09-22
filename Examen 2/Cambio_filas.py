def main():

    #Definimos la matriz dada
    matriz = [[8,3,24], [12,13,-11],[14,12,-6]]

    fila_1, fila_2 = solicitar_numeros()

    print(f"La matriz resultante al cambiar las filas es: {cambiar_filas(fila_1,fila_2, matriz)}")


def solicitar_numeros():
    #Declaramos esta variable como falsa para ingresar al while
    son_validos = False

    #Verifica si los valores ingresados estan en los rangos establecidos
    while son_validos == False:

        print("Debe ingresar valores enteros en el intervalo [0,2]")
        try:
            fila_1 = int(input("Digite el numero de una de las filas que desea cambiar: "))
            fila_2 = int(input("Digite el valor de la otra fila que desea cambiar: "))
        except: 
            print("Los valores de las filas no son válidos")
        else:
            #Verificamos que los dados esten en el intervalo [0,2]
            if (fila_1 >= 0 and fila_1 < 3) and (fila_2 >= 0 and fila_2 < 3):
                son_validos = True
            else:
                print("Los valores de las filas no son válidos")


    #Creamos una lista con los numeros ingresados por el usuario
    return fila_1, fila_2

#Esta funcion cambia las filas
def cambiar_filas(fila_1, fila_2, matriz):

    #Se crea una variable temporal que guarda una de las filas
    fila_temporal = matriz[fila_1].copy()

    #Se intercambian
    matriz[fila_1] = matriz[fila_2]
    matriz[fila_2] = fila_temporal

    return matriz


if __name__ == "__main__":
    main()
